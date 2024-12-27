// 封装canvas指纹
import CryptoJS from "crypto-js";
import { api } from "./api";

const myApi = api();

const hex_md5 = (str) => {
    const md5 = CryptoJS.MD5(str);
    return md5.toString();
};

const getCanvasData = () => {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    let txt = 'Nie Yu Guo Shi Ge Da Sha Bi.';
    ctx.textBaseline = 'top';
    // the most common type
    ctx.font = '14px Arial';
    ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = '#f60';
    ctx.fillRect(125,1,62,20);
    ctx.fillText(txt,2,15);
    ctx.fillStyle = 'rgba(102,204,0,0.7)';
    ctx.fillText(txt,4,17);
    return canvas.toDataURL();
};

const getCanvasFinger = () => {
    const canvasData = getCanvasData();
    const md5 = hex_md5(canvasData);
    localStorage.setItem('device-finger',md5);
    return md5;
};

const getFinger = () => {
    return localStorage.getItem('device-finger');
};

const getToken = () => {
    return localStorage.getItem('device-token');
};

const requestToken = async(finger) => {
    try {
        const finger_data = {'signature': finger};
        const token_res = await myApi.post('url', finger_data);
        localStorage.setItem('device-token', token_res.data.token);
        return token_res.data.token;
    } catch(err) {
        console.error('请求token失败',err);
    }
};

const checkToken = async() => {
    const token = getToken();
    if (!token) {
        const finger = getFinger() ? getFinger() : getCanvasFinger();
    }
}