import type { Metadata } from "next";
import localFont from "next/font/local";
import {Poppins} from 'next/font/google';
import "./globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

const poppins = Poppins({
  weight:["100" , "200", "300" , "400" , "500" , "600", "700" , "800", "900" ],
  subsets: ["latin"],

})

export const metadata: Metadata = {
  title: 'InvestGroup | IA mudando cenário de investimentos de formas que os investidores irão valorizar mais a qualidade dos ativos de IA de uma empresa ',
  description: 'IA mudando cenário de investimentos de formas que os investidores irão valorizar mais a qualidade dos ativos de IA de uma empresa ',
}
import { ToastContainer} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      
      <body
        className={`${geistSans.variable} ${poppins.className} ${geistMono.variable} antialiased`}
      >
        <ToastContainer /> 
        {children}
      </body>
    </html>
  );
}
