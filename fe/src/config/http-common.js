import axios from "axios";
axios.interceptors.request.use(config => {
    // //console.log(Vue.cookie.get("token"));
    config.url = `http://68.183.71.0:5000/${config.url}`;
    // //console.log(`${process.env.API_URL}`);
    config.headers = {
        "Content-Type": "application/json"
    };
    return config;
});
export const HTTP = axios;
