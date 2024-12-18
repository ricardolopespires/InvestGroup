import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";
import axios from "axios";

// Initialize variables for token and refresh token
let accessToken = "";
let refresh_token = "";

// Ensure localStorage is accessed only on the client-side (browser)
if (typeof window !== "undefined") {
  accessToken = localStorage.getItem("token") ? JSON.parse(localStorage.getItem("token")) : "";
  refresh_token = localStorage.getItem("refresh_token") ? JSON.parse(localStorage.getItem("refresh_token")) : "";
}

// Base URL for your API
const baseURL = "http://localhost:8000";

// Create an Axios instance
const AxiosInstance = axios.create({
  baseURL: baseURL,
  "Content-type": "application/json",
  headers: { Authorization: accessToken ? `Bearer ${accessToken}` : "" },
});

// Add request interceptor to check for token expiration
AxiosInstance.interceptors.request.use(async (req) => {
  if (typeof window !== "undefined" && accessToken) {
    // Check if token exists in localStorage and is valid
    req.headers.Authorization = `Bearer ${accessToken}`;

    const user = jwtDecode(accessToken);

    // Check if the token is expired
    const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;
    if (!isExpired) return req;

    // If token is expired, refresh the token using the refresh token
    try {
      const resp = await axios.post(`${baseURL}/api/v1/auth/token/refresh/`, {
        refresh: refresh_token,
      });

      // Store the new token in localStorage and update the request header
      if (typeof window !== "undefined") {
        localStorage.setItem("token", JSON.stringify(resp.data.access));
      }
      req.headers.Authorization = `Bearer ${resp.data.access}`;
      return req;
    } catch (error) {
      console.error("Token refresh failed:", error);
      return req;
    }
  } else {
    // If no accessToken, set Authorization to empty
    req.headers.Authorization = "";
    return req;
  }
});

export default AxiosInstance;
