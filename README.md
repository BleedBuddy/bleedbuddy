# Bleed Buddy - Deployment Guide

This guide will walk you step by step through setting up and deploying your Bleed Buddy app.

---

## 1. Prerequisites
- A **GitHub account** (free).
- A **Render.com account** (free tier is fine).
- A **Stripe account** (for payments).

---

## 2. Getting the Code to GitHub
1. Download the `bleed_buddy.zip` file and unzip it on your computer.
2. Go to [GitHub](https://github.com).
3. Log in and click the **+** in the top right → **New repository**.
4. Name it `bleed-buddy` (or whatever you prefer).
5. On your computer, unzip the folder. Drag and drop all files into your new GitHub repository using the GitHub web upload tool, OR use Git if you are comfortable.

Files included:
- `app.py`
- `requirements.txt`
- `Procfile`
- `.env.example`
- `templates/index.html`
- `subscribers.csv`

---

## 3. Deploying to Render
1. Go to [Render.com](https://render.com).
2. Click **New** → **Web Service**.
3. Connect your GitHub account if prompted.
4. Select your `bleed-buddy` repository.
5. Name the service `bleed-buddy`.
6. Choose **Free** plan for now.
7. **Environment: Python 3**.
8. In **Build Command**, type:
   ```bash
   pip install -r requirements.txt
   ```
9. In **Start Command**, type:
   ```bash
   gunicorn app:app
   ```
10. Click **Create Web Service**.

Render will now build and deploy your app.

---

## 4. Setting Environment Variables (Keys)
1. In Render, go to your service → **Environment** → **Add Environment Variable**.
2. Add the following (from your `.env.example`):
   - `STRIPE_PUBLISHABLE_KEY` → your pk_live_xxx
   - `STRIPE_SECRET_KEY` → your sk_live_xxx
   - `STRIPE_WEBHOOK_SECRET` → your whsec_xxx (from Stripe Dashboard > Developers > Webhooks)
3. Click **Save Changes** and redeploy.

---

## 5. Stripe Setup
1. Go to [Stripe Dashboard](https://dashboard.stripe.com).
2. Get your **Publishable** and **Secret** keys (start with test mode).
3. Create a **Webhook Endpoint** in Stripe:
   - URL: `https://your-render-domain.com/webhook`
   - Events: `checkout.session.completed`
4. Copy the **Webhook Secret** into Render as `STRIPE_WEBHOOK_SECRET`.

---

## 6. Test the App
1. Visit your Render app URL (something like `https://bleed-buddy.onrender.com`).
2. Try uploading a PDF/PNG/JPG file.
3. Click **Pay $5.99 & Convert** → Stripe test checkout will appear.
   - Use test card: `4242 4242 4242 4242`, any date, any CVC.
4. After success, you should be redirected back to your site.

---

## 7. Point Your Domain (Optional)
If you own `bleedbuddy.com` or another domain:
1. Go to your domain registrar (like Hostinger).
2. Find **DNS Settings**.
3. Add a **CNAME record** pointing `www` to your Render service URL.
4. In Render, add the custom domain in settings.

---

## 8. Next Steps
- Replace the mascot placeholder image in `templates/index.html` with your real design.
- Update text (FAQ, Testimonials, Policies) inside the HTML file if needed.
- Monitor file sizes and optimize for Render’s free tier.

---

## Support
If you get stuck:
- Check Render deploy logs.
- Check Stripe Dashboard logs for webhook events.
- Email hello@bleedbuddy.com (placeholder).

---

Enjoy using **Bleed Buddy**!
