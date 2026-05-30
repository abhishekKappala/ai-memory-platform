import "./globals.css";

import {
  ThemeProvider
} from "@/providers/theme-provider";

import {
  QueryProvider
} from "@/providers/query-provider";

export default function RootLayout({

  children,

}: Readonly<{

  children: React.ReactNode;

}>) {

  return (

    <html
      lang="en"
      suppressHydrationWarning
    >

      <body>

        <ThemeProvider>

          <QueryProvider>

            {children}

          </QueryProvider>

        </ThemeProvider>

      </body>

    </html>
  );
}