window.BASSEY_CONFIG = {
  paystackPublicKey: "pk_test_d394571743d63e0c35208183869a9d9c018ea691",   // pk_test_... from Paystack → Settings → API Keys & Webhooks
  verifyUrl: "https://bassey-pay.timmyberry738.workers.dev",
  bookingDeposit: 10000,
  whatsapp: "09065563764",        // your WhatsApp number, e.g. "08012345678"
  bank: { bankName: "OPay", accountName: "Timothy Olaomoju Oluwatosin", accountNumber: "9076818538" },   // shown to customers who pay by transfer
  firebase: {
    apiKey: "AIzaSyAuOSBmT9a4E3p7m7_3W7XYmcoM6pT73K8",
    authDomain: "bassey-stitches.firebaseapp.com",
    projectId: "bassey-stitches",
    storageBucket: "bassey-stitches.firebasestorage.app",
    messagingSenderId: "374531124855",
    appId: "1:374531124855:web:5bb9de4c1b0db0e66ba072"
  }
};
