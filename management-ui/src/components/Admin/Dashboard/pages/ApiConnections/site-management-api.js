import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_SITE_MANAGEMENT_API_URL,
  // baseURL: "http://0.0.0.0:8070/sites-man-api",
});

export default api;