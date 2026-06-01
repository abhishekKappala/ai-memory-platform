import axios from "axios";

console.log(
  "NEXT_PUBLIC_API_URL =",
  process.env.NEXT_PUBLIC_API_URL
);

export const api = axios.create({
  baseURL:
    process.env.NEXT_PUBLIC_API_URL,
});

api.interceptors.request.use(
  (config) => {

    const token =
      localStorage.getItem(
        "token"
      );

    if (token) {

      config.headers.Authorization =
        `Bearer ${token}`;
    }

    return config;
  }
);