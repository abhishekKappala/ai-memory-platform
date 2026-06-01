import Link from "next/link";

export default function HomePage() {

  return (

    <main
      className="
      min-h-screen
      flex
      flex-col
      items-center
      justify-center
      bg-background
      text-foreground
      px-6
      "
    >

      <div
        className="
        text-center
        max-w-3xl
        "
      >

        <h1
          className="
          text-5xl
          font-bold
          mb-6
          "
        >
          AI Memory Platform
        </h1>

        <p
          className="
          text-lg
          text-muted-foreground
          mb-10
          "
        >
          Persistent AI conversations
          with memory and context retrieval.
        </p>

        <div
          className="
          flex
          justify-center
          gap-4
          "
        >

          <Link
            href="/login"
            className="
            px-6
            py-3
            rounded-lg
            bg-white
            text-black
            font-medium
            hover:opacity-90
            transition
            "
          >
            Login
          </Link>

          <Link
            href="/register"
            className="
            px-6
            py-3
            rounded-lg
            border
            font-medium
            hover:bg-accent
            transition
            "
          >
            Register
          </Link>

        </div>

      </div>

    </main>
  );
}