import { api }
from "./api";

import {

  LoginPayload,

  RegisterPayload,

  AuthResponse

} from "@/types/auth";


export async function login(

  data:LoginPayload

){

  const form =
    new URLSearchParams();

  form.append(
    "username",
    data.email
  );

  form.append(
    "password",
    data.password
  );

  const response =
    await api.post<AuthResponse>(

      "/auth/login",

      form,

      {

        headers:{

          "Content-Type":
          "application/x-www-form-urlencoded"
        }
      }
    );

  return response.data;
}


export async function register(

  data:RegisterPayload
){

  const response =
    await api.post(

      "/auth/signup",

      data
    );

  return response.data;
}