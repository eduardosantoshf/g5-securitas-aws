import axios from "axios";

const api = axios.create({
  //baseURL: 'http://localhost:8070/sites-man-api',
  baseURL: process.env.REACT_APP_SITE_MANAGEMENT_API_URL,
});

export default api;