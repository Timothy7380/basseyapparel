/* Bassey Stitches site settings.
   Fill these in to switch on live payments and real accounts. Leave blank to keep preview mode. */
window.BASSEY_CONFIG = {
  // Paystack PUBLIC key (starts with pk_test_ or pk_live_). Never put the secret key (sk_...) here.
  paystackPublicKey: "",

  // Deposit charged when booking a fitting, in Naira.
  bookingDeposit: 10000,

  // Firebase web app config for sign in / sign up and "Continue with Google".
  // Paste the firebaseConfig object from Firebase console > Project settings > Your apps, e.g.
  // firebase: { apiKey: "...", authDomain: "....firebaseapp.com", projectId: "...", appId: "..." },
  firebase: null
};
