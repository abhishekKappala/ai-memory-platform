"use client";

import { useState } from "react";

import { useRouter } from "next/navigation";

import { register } from "@/services/auth-service";

export default function RegisterPage() {

  const router = useRouter();

  const [username, setUsername] =
    useState("");

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  async function handleRegister() {

    try {

      setLoading(true);

      await register({

        username,
        email,
        password

      });

      router.push("/login");

    } catch (error) {

      console.error(error);

      alert("Registration failed");

    } finally {

      setLoading(false);
    }
  }

  return (

    <main

      className="

      flex

      items-center

      justify-center

      min-h-screen

      bg-background

      text-foreground

    "

    >

      <div

        className="

        w-[380px]

        rounded-2xl

        border

        p-8

        space-y-5

        shadow-lg

        bg-background

      "

      >

        <div className="space-y-1">

          <h1

            className="

            text-3xl

            font-semibold

          "

          >

            Create account

          </h1>

          <p

            className="

            text-sm

            text-muted-foreground

          "

          >

            Start using your AI memory system

          </p>

        </div>

        <input

          placeholder="Username"

          value={username}

          onChange={(e)=>

            setUsername(e.target.value)
          }

          className="

          w-full

          rounded-lg

          border

          p-3

          bg-background

          "

        />

        <input

          placeholder="Email"

          type="email"

          value={email}

          onChange={(e)=>

            setEmail(e.target.value)
          }

          className="

          w-full

          rounded-lg

          border

          p-3

          bg-background

          "

        />

        <input

          placeholder="Password"

          type="password"

          value={password}

          onChange={(e)=>

            setPassword(e.target.value)
          }

          className="

          w-full

          rounded-lg

          border

          p-3

          bg-background

          "

        />

        <button

          onClick={handleRegister}

          disabled={loading}

          className="

          w-full

          rounded-lg

          bg-white

          text-black

          p-3

          font-medium

          transition-opacity

          hover:opacity-90

          disabled:opacity-50

          "

        >

          {

            loading

            ?

            "Creating..."

            :

            "Create Account"

          }

        </button>

      </div>

    </main>
  );
}