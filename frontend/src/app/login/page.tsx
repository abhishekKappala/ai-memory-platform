"use client";

import {

  useState

} from "react";

import {

  login

} from "@/services/auth-service";

import {

  useAuthStore

} from "@/store/auth-store";

import {

  useRouter

} from "next/navigation";


export default function LoginPage(){

  const router=
    useRouter();

  const setToken=
    useAuthStore(
      s=>s.setToken
    );

  const [email,setEmail]=
    useState("");

  const [

    password,

    setPassword

  ]=useState("");


  async function handleLogin(){

    try{

      const res=
        await login({

          email,

          password
        });

      setToken(
        res.access_token
      );

      router.push(
        "/chat"
      );

    }catch{

      alert(
        "Login failed"
      );
    }
  }

  return(

    <main

      className="

      flex

      items-center

      justify-center

      h-screen

    "

    >

      <div

        className="

        w-[350px]

        space-y-4

      "

      >

        <input

          className="
          w-full
          border
          p-3
          rounded-lg
          "

          placeholder="Email"

          onChange={(e)=>

            setEmail(
              e.target.value
            )
          }
        />

        <input

          type="password"

          className="
          w-full
          border
          p-3
          rounded-lg
          "

          placeholder="Password"

          onChange={(e)=>

            setPassword(
              e.target.value
            )
          }
        />

        <button

          onClick={
            handleLogin
          }

          className="

          w-full

          rounded-lg

          p-3

          bg-white

          text-black

          "

        >

          Login

        </button>

      </div>

    </main>
  );
}