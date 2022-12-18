import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_SITE_MANAGEMENT_API_URL,
});

export default api;