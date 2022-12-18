import axios from "axios";

const api = axios.create({
  //baseURL: 'http://localhost:8070/sites-man-api',
  //baseURL: process.env.REACT_APP_SITE_MANAGEMENT_API_URL,
  baseURL: "http://15.236.64.199/sites-man-api",

});

export default api;