import streamlit as st

# Judul aplikasi
st.title("💻 What's Your Perfect IT Role?")

# Input nama
nama = st.text_input("Masukkan nama kamu:")

# Pertanyaan-pertanyaan quiz
st.subheader("Yuk isi pertanyaan ini dulu!")

q1 = st.radio("1. Kamu lebih suka aktivitas yang seperti apa?", [
    "Ngulik data atau angka",
    "Jaga sistem biar tetap aman",
    "Bikin atau edit website",
    "Desain tampilan aplikasi/website",
    "Ngatur dan kerja bareng tim"
])

q2 = st.radio("2. Kalau lihat aplikasi atau website, kamu biasanya fokus ke...", [
    "Data yang ditampilkan",
    "Keamanan akun dan privasi",
    "Tampilan teknis atau loading-nya",
    "Desainnya enak dilihat atau nggak",
    "Alur dan susunan menunya"
])

q3 = st.radio("3. Kamu paling senang saat...", [
    "Bisa nemuin pola dari data",
    "Bantu orang biar akunnya nggak kena hack",
    "Ngoding dan lihat hasilnya muncul",
    "Desain sesuatu yang bikin orang betah",
    "Ngelola kerjaan tim biar lancar"
])

q4 = st.radio("4. Dalam kerja tim, kamu sering jadi orang yang...", [
    "Ngumpulin dan menganalisis info",
    "Cek dan pastiin semua aman",
    "Kerjain bagian teknis atau coding",
    "Bikin presentasi atau desain",
    "Ngatur jadwal dan komunikasi tim"
])

q5 = st.radio("5. Kamu bakal seneng kalau kerja yang bikin kamu...", [
    "Bisa lihat hasil dari analisis kamu",
    "Ngebantu orang tetap aman secara digital",
    "Bangun sesuatu dari nol",
    "Bikin pengalaman user makin nyaman",
    "Jadi penghubung antar orang & ide"
])

# Tombol submit
if st.button("Submit"):
    # Inisialisasi skor untuk setiap bidang profesi
    scores = {
        "Data Analyst": 0,
        "Cybersecurity Specialist": 0,
        "Web Developer": 0,
        "UI/UX Designer": 0,
        "Project Manager": 0
    }

    # Mengumpulkan semua jawaban user
    answers = [q1, q2, q3, q4, q5]

    # Logika penilaian berdasarkan keyword dalam jawaban
    for ans in answers:
        if "data" in ans.lower() or "angka" in ans.lower() or "analisis" in ans.lower():
            scores["Data Analyst"] += 1
        elif "aman" in ans.lower() or "hack" in ans.lower() or "privasi" in ans.lower():
            scores["Cybersecurity Specialist"] += 1
        elif "website" in ans.lower() or "ngoding" in ans.lower() or "bangun" in ans.lower():
            scores["Web Developer"] += 1
        elif "desain" in ans.lower() or "tampilan" in ans.lower() or "presentasi" in ans.lower():
            scores["UI/UX Designer"] += 1
        elif "tim" in ans.lower() or "ngatur" in ans.lower() or "komunikasi" in ans.lower():
            scores["Project Manager"] += 1

    # Tentukan hasil tertinggi
    job_result = max(scores, key=scores.get)

    # Gambar/GIF yang cocok
    job_images = {
        "Data Analyst": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnpyNWh5c2VkMGNpMTNqZW10ejI1azl2emM1Z2F2Z3dmNDl0eTdrZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SvckSy7fFviqrq8ClF/giphy.gif",
        "Cybersecurity Specialist": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGFxNmw0aGtwaHp4dnB6dWRvYmx3bzV3MjlleWlvbTc0bmVtdTY1MSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/RDZo7znAdn2u7sAcWH/giphy.gif",
        "Web Developer": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTJ3amtpbmNka2NnbnZjcTZ5ZnZsd2NjMmlkMHZpcXlnanJpZWRrYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/iT0XxjFbxDO2xdpTWw/giphy.gif",
        "UI/UX Designer": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzB0dGQyYmozNDJwM2N1NGszeDZmOWVnZ2ltdmU3eGM0bm5paGI4ayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fvf71YSL7vymjQrpHE/giphy.gif",
        "Project Manager": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGoyc3IxYWJ3OG53dDJ6anAxanhpYWlpdjJnZ29qbHV1bDZ4Yng2NiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Tjq0NVePKbXUDqFHxC/giphy.gif"
    }

    job_desc = {
        "Data Analyst": "kamu suka berpikir logis dan jago menemukan pola tersembunyi dari data.",
        "Cybersecurity Specialist": "kamu waspada dan peduli sama keamanan digital.",
        "Web Developer": "kamu senang membangun sesuatu dari nol dan lihat hasil nyata.",
        "UI/UX Designer": "kamu punya rasa seni dan empati tinggi buat bikin pengalaman pengguna jadi nyaman.",
        "Project Manager": "kamu pandai mengatur orang dan waktu, cocok mimpin proyek!"
    }

    st.markdown(f"### Hi **{nama}**! 👋")
    st.success(f"Berdasarkan jawaban kamu, {job_desc[job_result]}")
    st.markdown(f"<h3 style='text-align:center; font-weight:bold;'>Kamu cocok jadi: {job_result}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
                <div style='text-align:center;'>
                <img src='{job_images[job_result]}' style='max-width: 400px; width: 100%; height: auto;'>
                </div>
                """, unsafe_allow_html=True)
    st.balloons()
    st.markdown("""
                <div style='text-align:center; margin-top:30px;'>
                <p>Terima kasih sudah ikut quiz! Semoga bermanfaat untuk menentukan karier IT kamu!</p>
                <p>Selamat berkarier di dunia IT! 🚀</p>
                </div>
                """, unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("Dibuat sambil ngopi ☕ oleh zaimaasshafa")