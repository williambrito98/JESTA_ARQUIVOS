export default async function (puppeteer, config) {
    let browser;
    let page;


    browser = await puppeteer.launch({
        executablePath: config.pathChrome,
        headless: true,
        defaultViewport: {
            width: 1200,
            height: 1080
        },
        slowMo: 20
    });

    page = await browser.newPage();

    page.setDefaultTimeout(80000);
    page.setDefaultNavigationTimeout(80000);

    await page._client.send('Page.setDownloadBehavior', {
        behavior: 'allow',
        downloadPath: config.pathDownload
    })


    return { browser, page };
}