import puppeteer from 'puppeteer-core';
import path from 'path';
import fs from 'fs';
import initBrowser from './CreateBrowser.js';
import { exec } from 'child_process';
const __dirname = path.resolve();
const config = JSON.parse(fs.readFileSync(path.join(__dirname, 'config.json')));
const pythonExec = path.join(__dirname, 'ExtractFiles', 'index.py');
config.pathDownload = path.join(__dirname, 'downloads');
(async () => {
    console.log("INICIANDO BROWSER");
    const { browser, page } = await initBrowser(puppeteer, config);
    console.log("BROWSER INICIADO");
    await page.goto('https://app.jettax.com.br/login', { waitUntil: 'networkidle0' });
    await page.waitForSelector('#contato-email');
    await page.type('#contato-email', config.user);
    await page.type('#contato-senha', config.password);
    await page.click('#loginForm > div.card-rodape > button');
    await page.waitForTimeout(12000);
    await page.click('body > div._hj-widget-container._hj-widget-theme-dark > div > div > div._hj-1uMrd__styles__modal > button').catch(e => console.log('SEM QUESTIONARIO'))
    await page.evaluate(() => {
        document.querySelector('body > div.sweet-alert.sweetalert-notification.showSweetAlert.visible').style.display = 'none'
        document.querySelector('body > div.sweet-overlay').style.display = 'none'
    }).catch(e => console.log('SEM MODAL'));
    const numberOfFolder = await page.$$eval('body > div.mn-content.fixed-sidebar > main > div.col.s12.m12.l12 > div > div.col.s12.m12.l12 > div > div > table > tbody > tr', item => item.length);
    console.log("BAIXANDO ARQUIVOS");
    let filesZipToRename = [];
    let nameZip, typeZip;
    for (let index = 1; index <= numberOfFolder; index++) {
        nameZip = await page.$eval(`body > div.mn-content.fixed-sidebar > main > div.col.s12.m12.l12 > div > div.col.s12.m12.l12 > div > div > table > tbody > tr:nth-child(${index})  > td:nth-child(7) > a`, item => item.href.match(/package_.+\.zip/)[0]);
        typeZip = await page.$eval(`body > div.mn-content.fixed-sidebar > main > div.col.s12.m12.l12 > div > div.col.s12.m12.l12 > div > div > table > tbody > tr:nth-child(${index}) > td:nth-child(2)`, item => item.textContent.split(' ').join('_'));
        filesZipToRename[nameZip] = typeZip;
        await page.click(`body > div.mn-content.fixed-sidebar > main > div.col.s12.m12.l12 > div > div.col.s12.m12.l12 > div > div > table > tbody > tr:nth-child(${index})  > td:nth-child(7) > a`);
        await page.waitForTimeout(5000);
    }
    console.log("ESPERANDO DOWNLOAD DOS ARQUIVOS");
    let wasDownloaded = false;
    while (!wasDownloaded) {
        fs.readdirSync(config.pathDownload).map(item => {
            if (!item.includes('crdownload')) {
                wasDownloaded = true;
                return
            }
        })
        await page.waitForTimeout(5000);
    }
    let value;
    for (var key in filesZipToRename) {
        value = filesZipToRename[key];
        fs.renameSync(path.join(config.pathDownload, key), path.join(config.pathDownload, value) + '.zip');
    }
    console.log("EXECUTANDO PYTHON");
    exec(`python ExtractFiles/index.py`, (error, stdout, stderr) => {
        if (error) throw new Error('erro ao executar python ' + error)
        console.log(stdout);
        console.log(stderr);
        process.exit();
    });

})();
