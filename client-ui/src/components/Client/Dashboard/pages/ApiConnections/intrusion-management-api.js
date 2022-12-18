import axios from "axios";

const api = axios.create({

  baseURL: process.env.REACT_APP_INTRUSION_MANAGEMENT_API_URL,

});

export const apiBaseUrl = process.env.REACT_APP_INTRUSION_MANAGEMENT_API_URL;

export default api;