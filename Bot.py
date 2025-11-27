from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime
import pytz
import os

TOKEN = ""

paises = {
    "🇧🇷 Brasil (São Paulo)": "America/Sao_Paulo",
    "🇧🇷 Brasil (Manaus)": "America/Manaus",
    "🇦🇷 Argentina": "America/Argentina/Buenos_Aires",
    "🇨🇱 Chile": "America/Santiago",
    "🇺🇾 Uruguai": "America/Montevideo",
    "🇵🇾 Paraguai": "America/Asuncion",
    "🇧🇴 Bolívia": "America/La_Paz",
    "🇨🇴 Colômbia": "America/Bogota",
    "🇵🇪 Peru": "America/Lima",
    "🇪🇨 Equador": "America/Guayaquil",
    "🇲🇽 México": "America/Mexico_City",

    "🇺🇸 EUA (New York)": "America/New_York",
    "🇺🇸 EUA (Los Angeles)": "America/Los_Angeles",
    "🇨🇦 Canadá (Toronto)": "America/Toronto",
    "🇨🇦 Canadá (Vancouver)": "America/Vancouver",

    "🇬🇧 Inglaterra": "Europe/London",
    "🇫🇷 França": "Europe/Paris",
    "🇩🇪 Alemanha": "Europe/Berlin",
    "🇮🇹 Itália": "Europe/Rome",
    "🇪🇸 Espanha": "Europe/Madrid",
    "🇵🇹 Portugal": "Europe/Lisbon",
    "🇳🇱 Holanda": "Europe/Amsterdam",
    "🇧🇪 Bélgica": "Europe/Brussels",
    "🇨🇭 Suíça": "Europe/Zurich",
    "🇸🇪 Suécia": "Europe/Stockholm",
    "🇳🇴 Noruega": "Europe/Oslo",
    "🇩🇰 Dinamarca": "Europe/Copenhagen",
    "🇫🇮 Finlândia": "Europe/Helsinki",
    "🇵🇱 Polônia": "Europe/Warsaw",

    "🇷🇺 Rússia (Moscou)": "Europe/Moscow",
    "🇹🇷 Turquia": "Europe/Istanbul",

    "🇯🇵 Japão": "Asia/Tokyo",
    "🇨🇳 China": "Asia/Shanghai",
    "🇰🇷 Coreia do Sul": "Asia/Seoul",
    "🇮🇳 Índia": "Asia/Kolkata",
    "🇮🇩 Indonésia": "Asia/Jakarta",
    "🇸🇬 Singapura": "Asia/Singapore",
    "🇦🇪 Emirados Árabes": "Asia/Dubai",

    "🇦🇺 Austrália (Sydney)": "Australia/Sydney",
    "🇳🇿 Nova Zelândia": "Pacific/Auckland"
}


keyboard = ReplyKeyboardMarkup(
    [[p] for p in paises.keys()],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Escolha um país para ver a hora:", reply_markup=keyboard)

async def receber_resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pais = update.message.text
    if pais not in paises:
        await update.message.reply_text("País inválido. Escolha um botão.")
        return

    tz = pytz.timezone(paises[pais])
    agora = datetime.now(tz).strftime("%d/%m/%Y • %H:%M:%S")

    await update.message.reply_text(f"🕒 Hora em {pais}:\n{agora}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, receber_resposta))
    app.run_polling()

if __name__ == "__main__":
    main()
