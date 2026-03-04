import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="İngilizce Kelime Sınavı", layout="centered")

# Kelime Havuzu
word_pool = [
    {"en": "On time", "tr": "Zamanında"}, {"en": "Calm", "tr": "Sakin, serin"}, {"en": "Teach", "tr": "Öğretmek"},
    {"en": "Pen Pal", "tr": "Mektup arkadaşı"}, {"en": "Messy", "tr": "Kirli"}, {"en": "Believe", "tr": "İnanmak"},
    {"en": "Kind", "tr": "Kibar"}, {"en": "Boost", "tr": "Yükseltmek"}, {"en": "Plant", "tr": "Bitki"},
    {"en": "Patient", "tr": "Hasta"}, {"en": "Serious", "tr": "Ciddi"}, {"en": "Skill", "tr": "Yetenekli"},
    {"en": "Find", "tr": "Bulmak"}, {"en": "Foreign", "tr": "Yabancı"}, {"en": "Author", "tr": "Yazar"},
    {"en": "Express", "tr": "Hızlı"}, {"en": "Amount", "tr": "Miktar"}, {"en": "Responsibility", "tr": "Sorumluluk"},
    {"en": "Care", "tr": "His"}, {"en": "Knitting", "tr": "Örgü örmek"}, {"en": "Interest", "tr": "İlgi, merak"},
    {"en": "Idea", "tr": "Fikir"}, {"en": "Solve", "tr": "Çözmek"}, {"en": "Trouble", "tr": "Problem"},
    {"en": "Invent", "tr": "İcat etmek"}, {"en": "Spend", "tr": "Para harca."}, {"en": "Other", "tr": "Diğeri"},
    {"en": "Brain", "tr": "Beyin"}, {"en": "Harmony", "tr": "Uyum"}, {"en": "Thought", "tr": "Düşünce"},
    {"en": "Outgoing", "tr": "Sosyal"}, {"en": "Laugh", "tr": "Güldürmek"}, {"en": "Seems", "tr": "Görünmek"},
    {"en": "Ahead", "tr": "İleri"}, {"en": "Move", "tr": "Hareket etmek"}, {"en": "Confusing", "tr": "Kafası karışmış"},
    {"en": "Pawn", "tr": "Piyon"}, {"en": "Knight", "tr": "Şövalye, Vezir"}, {"en": "Piece", "tr": "Parça"},
    {"en": "Differently", "tr": "Farklı"}, {"en": "Mistake", "tr": "Hata"}, {"en": "Rush", "tr": "Hızlı / Acele etmek"},
    {"en": "Dangerous", "tr": "Tehlikeli"}, {"en": "Safe", "tr": "Güvenli"}, {"en": "Standing", "tr": "Ayakta dur."},
    {"en": "Careful", "tr": "Dikkatli olmak"}, {"en": "Fall", "tr": "Düşmek"}, {"en": "Hit", "tr": "Vurmak"},
    {"en": "Better", "tr": "Daha iyi"}, {"en": "Shore", "tr": "Kıyı, sahil"}, {"en": "Coast", "tr": "Sahil / Kıyı"},
    {"en": "Dreamy", "tr": "Hayali"}, {"en": "Land", "tr": "Kara, toprak arazi"}, {"en": "Away", "tr": "Uzaklığında"},
    {"en": "Hooray", "tr": "Yaşasın"}, {"en": "Streets", "tr": "Sokak"}, {"en": "Full", "tr": "Dolu"},
    {"en": "Road", "tr": "Yol"}, {"en": "Stone", "tr": "Taş"}, {"en": "Materials", "tr": "Araç gereç"},
    {"en": "Spirit", "tr": "Huzurlu Ruh"}, {"en": "Baker", "tr": "Fırıncı"}, {"en": "Decorating", "tr": "Süsleme"},
    {"en": "Cabinet", "tr": "Raf"}, {"en": "Display", "tr": "Sergilemek"}, {"en": "Keep", "tr": "Tutmak / Bone"},
    {"en": "Wear", "tr": "Giyinmek"}, {"en": "Smell", "tr": "Koku"}, {"en": "Pastry", "tr": "Unlu mamüller"},
    {"en": "Butcher", "tr": "Kasap"}, {"en": "Line", "tr": "Sıra"}, {"en": "Florist", "tr": "Çiçekçi"},
    {"en": "Field", "tr": "Tarla / Alan"}, {"en": "Picking", "tr": "Toplanmak"}, {"en": "Prepare", "tr": "Hazırlamak"},
    {"en": "Give up", "tr": "Vazgeçmek"}, {"en": "Belong", "tr": "Ait olmak"}, {"en": "Artwork", "tr": "Sanat eseri"},
    {"en": "Thirsty", "tr": "Susamak"}, {"en": "Each", "tr": "Her biri"}, {"en": "Company", "tr": "Şirket"},
    {"en": "Gas station", "tr": "Benzinlik"}, {"en": "Vitamins", "tr": "Vitamin"}, {"en": "Explains", "tr": "Açıklamak"},
    {"en": "Answer", "tr": "Cevap"}, {"en": "Freedom", "tr": "Özgürlük"}, {"en": "Sympathy", "tr": "Sempati"},
    {"en": "Power", "tr": "Güç"}, {"en": "Opinions", "tr": "Fikir"}, {"en": "Instructions", "tr": "Klavuz vb."},
    {"en": "Town square", "tr": "Şehir merkezi"}, {"en": "Beauty", "tr": "Güzellik"}, {"en": "Busy", "tr": "Meşgul"},
    {"en": "Knowledge", "tr": "Bilgi"}, {"en": "Relative", "tr": "Akraba"}, {"en": "Compass", "tr": "Pusula"},
    {"en": "Niece", "tr": "Kız yeğen"}, {"en": "Prefer", "tr": "Tercih et."}, {"en": "Living", "tr": "Yaşamak"},
    {"en": "Need", "tr": "İhtiyaç"}, {"en": "Pharmacy", "tr": "Eczane"}, {"en": "Still", "tr": "Hala"},
    {"en": "Reality", "tr": "Gerçeklik"}, {"en": "Escalators", "tr": "Yürüyen m."}, {"en": "Herbs", "tr": "Bitki, baharat"},
    {"en": "Pipes", "tr": "Pipet"}, {"en": "Piles", "tr": "Yığıl"}, {"en": "Means", "tr": "Cimri"},
    {"en": "Practice", "tr": "Geliştirmek"}, {"en": "Miss", "tr": "Özlemek, kaçırmak, bekar"}, {"en": "Tell", "tr": "Anlatmak"},
    {"en": "Glad", "tr": "Memnun"}, {"en": "Available", "tr": "Müsait"}, {"en": "Mayor", "tr": "Belediye başkanı"},
    {"en": "Relation", "tr": "İlişki"}, {"en": "Nephew", "tr": "Erkek yeğen"}, {"en": "Parent", "tr": "Ebeveyn"},
    {"en": "Principal", "tr": "Müdür"}, {"en": "Twin", "tr": "İkiz"}, {"en": "Leisure time", "tr": "Boş zaman"},
    {"en": "Novel", "tr": "Roman"}, {"en": "Break", "tr": "Mola"}, {"en": "Schedule", "tr": "Program"},
    {"en": "Manage", "tr": "Başarmak"}, {"en": "Climate change", "tr": "İklim değişikliği"}, {"en": "Immediate", "tr": "Yakın"},
    {"en": "Worst", "tr": "En kötü"}, {"en": "Meet", "tr": "Toplantı / Buluşmak"}, {"en": "Future", "tr": "Gelecek"},
    {"en": "Crowded", "tr": "Kalabalık"}, {"en": "Pavement", "tr": "Kaldırım"}, {"en": "Pedestrians", "tr": "Yaya"},
    {"en": "President", "tr": "Sınıf başkanı"}, {"en": "Awful", "tr": "Dehşet verici"}, {"en": "Lost", "tr": "Kaybetmek"},
    {"en": "Mean", "tr": "Anlamına"}, {"en": "Teammate", "tr": "Takım ar."}, {"en": "Spare time", "tr": "Boş vakit"},
    {"en": "Cool", "tr": "Serin"}, {"en": "Graphic", "tr": "Çizgi, grafik"}, {"en": "Sound", "tr": "Ses"},
    {"en": "Bit", "tr": "Az"}, {"en": "Effect", "tr": "Etki"}, {"en": "Share", "tr": "Paylaşmak"},
    {"en": "Spot", "tr": "Alan"}, {"en": "Get tired", "tr": "Yorulmak"}, {"en": "Meeting", "tr": "Tanışmak"},
    {"en": "Complaint", "tr": "Şikayet"}, {"en": "Chaos", "tr": "Kaus"}, {"en": "Sidewalk", "tr": "Kaldırım"},
    {"en": "Put", "tr": "Koymak"}, {"en": "Pay", "tr": "Ödemek"}, {"en": "ALONE", "tr": "Yalnız"},
    {"en": "Unfamiliar", "tr": "Tanınmadık"}, {"en": "To care of", "tr": "İlgilenmek"}, {"en": "Only", "tr": "Yalnız, Tek"},
    {"en": "Arrived", "tr": "Ulaşmak"}, {"en": "Felt", "tr": "Hissetti"}, {"en": "Thanks to", "tr": "Sayesinde"},
    {"en": "Trip", "tr": "Seyehat"}, {"en": "Excited", "tr": "Heyecanlı"}, {"en": "Upon", "tr": "Üzerine"},
    {"en": "Famous", "tr": "Ünlü"}, {"en": "Hometown", "tr": "Memleket"}, {"en": "Climb", "tr": "Tırmanmak"},
    {"en": "Return", "tr": "Geri dönmek"}, {"en": "Split", "tr": "Bölmek"}, {"en": "Worried", "tr": "Endişeli"},
    {"en": "Beside", "tr": "Yanında"}, {"en": "Just", "tr": "Sadece"}, {"en": "Specific", "tr": "Özel"},
    {"en": "Separated", "tr": "Ayrılmak"}, {"en": "Stomach", "tr": "Karın, mide"}, {"en": "Thankfully", "tr": "Çok şükür"},
    {"en": "Track", "tr": "İzlemek"}, {"en": "Case", "tr": "Dava"}, {"en": "Soon", "tr": "Yakında"},
    {"en": "Crow", "tr": "Karga"}, {"en": "Down", "tr": "Aşağı"}, {"en": "Suddenly", "tr": "Birden"},
    {"en": "Discover", "tr": "Keşfetmek"}, {"en": "Explain", "tr": "Açıklamak"}, {"en": "Heard", "tr": "Duyulmuş"},
    {"en": "Sight", "tr": "Görünüş"}, {"en": "Could", "tr": "Olabilir"}, {"en": "Comic", "tr": "Komik"},
    {"en": "Huge", "tr": "Büyük / Devasa"}, {"en": "Playwright", "tr": "Oyun yaz."}, {"en": "Nearly", "tr": "Neredeyse"},
    {"en": "Theaters", "tr": "Tiyatro"}, {"en": "Sign", "tr": "Tabela / İşaret"}, {"en": "Hang", "tr": "Asmak"},
    {"en": "Front", "tr": "Ön"}, {"en": "Waiter", "tr": "Garson"}, {"en": "Twist", "tr": "Döndürmek"},
    {"en": "Each time", "tr": "Her defasında"}, {"en": "Fork", "tr": "Çatal"}, {"en": "Another", "tr": "Başka"},
    {"en": "Bratwurst", "tr": "Sosis"}, {"en": "Pick up", "tr": "Toplamak"}, {"en": "Well", "tr": "İyi"},
    {"en": "Gift", "tr": "Hediye"}, {"en": "Bought", "tr": "Satın almak"}, {"en": "Present", "tr": "Hediye"},
    {"en": "Decide", "tr": "Karar vermek"}, {"en": "Clap", "tr": "Alkışlamak"}, {"en": "Seat", "tr": "Oturak"},
    {"en": "Wave", "tr": "Dalga"}, {"en": "Sell", "tr": "Satmak"}, {"en": "Vacation", "tr": "Tatil"},
    {"en": "Hang out", "tr": "Takılmak"}, {"en": "Jealous", "tr": "Kıskanç"}, {"en": "Nap", "tr": "Şekerleme"},
    {"en": "Happen", "tr": "Olmak"}, {"en": "Occur", "tr": "Olmak"}, {"en": "Broken", "tr": "Bozuldu"},
    {"en": "Informal", "tr": "Gayriresmi"}, {"en": "Information", "tr": "Bilgi"}, {"en": "Receive", "tr": "Almak"},
    {"en": "Imagine", "tr": "Hayal et."}, {"en": "Response", "tr": "Cevap"}, {"en": "Carefully", "tr": "Dikkatlice"},
    {"en": "Sender", "tr": "Gönderici / Alıcı"}, {"en": "Since", "tr": "...'den beri"}, {"en": "Pool", "tr": "Havuz"},
    {"en": "XOXO", "tr": "Sarılıyorum ve ö."}, {"en": "Reaction", "tr": "Tepki"}, {"en": "Snooze Button", "tr": "Erteleme"},
    {"en": "Nervous", "tr": "Gergin, Titreşimli"}, {"en": "Rude", "tr": "Kaba"}, {"en": "Conversation", "tr": "Dialog"},
    {"en": "Descriptions", "tr": "Tarif"}, {"en": "Appearance", "tr": "Dış görünüş"}, {"en": "Personality", "tr": "Karakter"},
    {"en": "Blond", "tr": "Sarışın"}, {"en": "Verb", "tr": "Fiil"}, {"en": "Noun", "tr": "İsim"},
    {"en": "Adjective", "tr": "Sıfat"}, {"en": "Generous", "tr": "Cömert"}, {"en": "Honest", "tr": "Dürüst"},
    {"en": "Selfish", "tr": "Cimri"}, {"en": "Confident", "tr": "Öz güvenli"}, {"en": "Live", "tr": "Yaşamak"},
    {"en": "Job", "tr": "İş"}, {"en": "Excellent", "tr": "Mükemmel"}, {"en": "Provide", "tr": "Sağlamak"},
    {"en": "Necessary", "tr": "Gerekli"}, {"en": "Comfortable", "tr": "Konfor, rahat"}, {"en": "One of", "tr": "Biri"},
    {"en": "Bookshop", "tr": "Kitapevi"}, {"en": "Grab", "tr": "Almak"}, {"en": "Topic", "tr": "Konu"},
    {"en": "Include", "tr": "İçermek"}, {"en": "Fiction", "tr": "Kurgu"}, {"en": "Host", "tr": "Hizmet v."},
    {"en": "Event", "tr": "Davet"}, {"en": "Staff", "tr": "Değnek"}, {"en": "Equipment", "tr": "Ekipm."},
    {"en": "Gather", "tr": "Toplanmak"}, {"en": "In conclusion", "tr": "Özetle"}, {"en": "Because of", "tr": "Yüzünden"},
    {"en": "Effort", "tr": "Çaba"}, {"en": "Affair", "tr": "Çaba / Mesele"}, {"en": "Measured", "tr": "Ölçmek"},
    {"en": "Similar", "tr": "Benzer"}, {"en": "Degree", "tr": "Derece"}, {"en": "Excellence", "tr": "Üstünlük"},
    {"en": "Most", "tr": "En çok"}, {"en": "Summarized", "tr": "Özet"}, {"en": "Sleepover", "tr": "Gece kalma"},
    {"en": "However", "tr": "Bu şekilde / Ancak"}, {"en": "Emergency", "tr": "Acil durum"}, {"en": "Hollow", "tr": "Çukur"},
    {"en": "Shell", "tr": "Deniz kabuğu"}, {"en": "Ancient", "tr": "Eski"}, {"en": "Drip", "tr": "Damla"},
    {"en": "Solid", "tr": "Katı"}, {"en": "Hole", "tr": "Delik"}, {"en": "Cover", "tr": "Kaplamak"},
    {"en": "Call", "tr": "Adlandırmak"}, {"en": "Visitor", "tr": "Ziyaretçi"}, {"en": "Tour guide", "tr": "Rehber"},
    {"en": "Hurt", "tr": "Yaralanmak"}, {"en": "Helmet", "tr": "Kask"}, {"en": "Crawl", "tr": "Emeklemek"},
    {"en": "Tight", "tr": "Dar"}, {"en": "Ceiling", "tr": "Tavan"}, {"en": "Feet", "tr": "Yükseklik birimi"},
    {"en": "Us", "tr": "Siz, biz"}, {"en": "Moss", "tr": "Yosun"}, {"en": "Salamander", "tr": "Semender"},
    {"en": "Cricket", "tr": "Ateş Böceği"}, {"en": "Dweller", "tr": "Mağara Sakini"}, {"en": "Litter", "tr": "Çöp"},
    {"en": "Trash", "tr": "Çöp"}, {"en": "Garbage", "tr": "Çöp"}, {"en": "Waste", "tr": "Çöp"},
    {"en": "Spelunker", "tr": "Keşif"}, {"en": "Stalactite", "tr": "Sarkıt"}, {"en": "Stalagmite", "tr": "Dikit"},
    {"en": "Lantern", "tr": "Lamba"}, {"en": "Reason", "tr": "Sebep"}, {"en": "Below", "tr": "Aşağı"},
    {"en": "Rock", "tr": "Taş"}, {"en": "Sweater", "tr": "Kazak"}, {"en": "Without", "tr": "Sız - siz"},
    {"en": "Elbow Pad", "tr": "Dirseklik"}, {"en": "Shine", "tr": "Parlamak"}, {"en": "Creak", "tr": "Gıcırtı"},
    {"en": "Wild life", "tr": "Vahşi hayat"}, {"en": "Extraordinary", "tr": "Olağanüstü"}, {"en": "Ordinary", "tr": "Sıradan"},
    {"en": "Journey", "tr": "Seyahat"}, {"en": "Impressive", "tr": "Etkili"}, {"en": "Ship", "tr": "Gemi"},
    {"en": "Treasure", "tr": "Hazine"}, {"en": "Valuable", "tr": "Değerli"}, {"en": "Goods", "tr": "Mal"},
    {"en": "Silk", "tr": "İpek"}, {"en": "Major", "tr": "Büyük"}, {"en": "Fleet", "tr": "Filo"},
    {"en": "Enormous", "tr": "Kocaman"}, {"en": "Develop", "tr": "Gelişme"}, {"en": "Trade", "tr": "Takas"},
    {"en": "Epic", "tr": "Destansı"}, {"en": "Expedition", "tr": "Sefer"}, {"en": "Reach", "tr": "Ulaşmak"},
    {"en": "South", "tr": "Güney / Batı"}, {"en": "East", "tr": "Doğu"}, {"en": "North", "tr": "Kuzey"},
    {"en": "Spread", "tr": "Sürmek, yaymak"}, {"en": "Establish", "tr": "Kurmak"}, {"en": "Tie", "tr": "Bağ, ilişki, bağlar"},
    {"en": "Benefited", "tr": "Fayda, yarar"}, {"en": "Political", "tr": "Politik"}, {"en": "Pole", "tr": "Kutup"},
    {"en": "Common", "tr": "Sıradan"}, {"en": "Voyage", "tr": "Seyahat"}, {"en": "Although", "tr": "-e rağmen"},
    {"en": "Death", "tr": "Ölüm"}, {"en": "Legacy", "tr": "Efsane"}, {"en": "Last", "tr": "Vakit sürmek"},
    {"en": "Impact", "tr": "Efekt"}, {"en": "Continent", "tr": "Kıta"}, {"en": "Global", "tr": "Küresel"},
    {"en": "Mark", "tr": "İşaret"}, {"en": "Asia", "tr": "Asya"}, {"en": "Europe", "tr": "Avrupa"},
    {"en": "Africa", "tr": "Afrika"}, {"en": "South America", "tr": "Güney Amerika"}, {"en": "North America", "tr": "Kuzey Amerika"},
    {"en": "Australia", "tr": "Avustralya"}
]

# Session State Ayarları (Sayfa yenilendiğinde verilerin kaybolmaması için)
if 'quiz_active' not in st.session_state:
    st.session_state.quiz_active = False
    st.session_state.quiz_data = []
    st.session_state.start_time = None
    st.session_state.submitted = False
    st.session_state.score = 0

def start_new_quiz():
    selected_words = random.sample(word_pool, min(90, len(word_pool)))
    quiz_data = []
    
    for word in selected_words:
        wrong_options = [w["tr"] for w in word_pool if w["en"] != word["en"]]
        wrong_choices = random.sample(wrong_options, 3)
        options = wrong_choices + [word["tr"]]
        random.shuffle(options)
        
        quiz_data.append({
            "question": word["en"],
            "correct": word["tr"],
            "options": options
        })
        
    st.session_state.quiz_data = quiz_data
    st.session_state.quiz_active = True
    st.session_state.submitted = False
    st.session_state.score = 0
    st.session_state.start_time = time.time()

st.title("📚 İngilizce Kelime Sınavı")

# Ana Ekran
if not st.session_state.quiz_active and not st.session_state.submitted:
    st.write("Sınav **90 sorudan** oluşmaktadır ve hedef süre **45 dakikadır**.")
    if st.button("Yeni Quiz Oluştur ve Başla", type="primary"):
        start_new_quiz()
        st.rerun()

# Sınav Ekranı
if st.session_state.quiz_active and not st.session_state.submitted:
    
    # Kalan saniyeyi hesaplayıp JavaScript'e gönderiyoruz
    time_elapsed = time.time() - st.session_state.start_time
    time_left_seconds = int(45 * 60 - time_elapsed)
    if time_left_seconds < 0:
        time_left_seconds = 0

    # CANLI SAYAÇ HTML/JS KODU (Ortalanmış)
    timer_html = f"""
    <div style="
        position: fixed; 
        top: 20px; 
        left: 50%; 
        transform: translateX(-50%);
        background: #ffffff; 
        padding: 10px 25px; 
        border-radius: 8px; 
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15); 
        border: 2px solid #ff4b4b; 
        color: #ff4b4b; 
        font-weight: bold; 
        font-size: 1.2rem; 
        z-index: 99999;
        text-align: center;
        white-space: nowrap;">
        ⏳ Kalan Süre: <span id="countdown_timer">Hesaplanıyor...</span>
    </div>

    <script>
        var timeLeft = {time_left_seconds};
        var elem = window.parent.document.getElementById('countdown_timer');
        if (!elem) elem = document.getElementById('countdown_timer'); // Yedek plan
        
        // Önceki sayaç varsa temizle (Streamlit yeniden yüklemeleri için)
        if (window.countdownInterval) clearInterval(window.countdownInterval);
        
        window.countdownInterval = setInterval(function() {{
            if (timeLeft <= 0) {{
                clearInterval(window.countdownInterval);
                if(elem) elem.innerHTML = "00:00 - Süre Bitti!";
            }} else {{
                var m = Math.floor(timeLeft / 60);
                var s = timeLeft % 60;
                if(elem) elem.innerHTML = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
                timeLeft--;
            }}
        }}, 1000);
    </script>
    """
    
    # HTML'i sayfaya enjekte et (yukarıda sabit ve ortalanmış kalacak)
    st.markdown(timer_html, unsafe_allow_html=True)
    
    st.info("Sınav başladı! Kalan süreni ekranın en üstünde görebilirsin.")
    
    with st.form("quiz_form"):
        user_answers = []
        for i, q in enumerate(st.session_state.quiz_data):
            st.markdown(f"**{i + 1}. \"{q['question']}\" kelimesinin Türkçe karşılığı nedir?**")
            ans = st.radio(f"Soru {i+1}", q['options'], key=f"q_{i}", index=None, label_visibility="collapsed")
            user_answers.append(ans)
            st.write("---")
            
        submit_button = st.form_submit_button("Sınavı Bitir ve Puanı Gör")
        
        if submit_button:
            elapsed_time = time.time() - st.session_state.start_time
            st.session_state.elapsed_minutes = int(elapsed_time // 60)
            
            score = sum(1 for i, q in enumerate(st.session_state.quiz_data) if user_answers[i] == q['correct'])
            st.session_state.score = score
            st.session_state.submitted = True
            st.session_state.quiz_active = False
            st.rerun()

# Sonuç Ekranı
if st.session_state.submitted:
    st.success("Sınav Tamamlandı!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Puanınız", value=f"{st.session_state.score} / 90")
    with col2:
        st.metric(label="Harcanan Süre", value=f"{st.session_state.elapsed_minutes} Dakika")
        
    if st.session_state.elapsed_minutes >= 45:
        st.error("Hedeflenen 45 dakikalık süreyi aştınız.")
    else:
        st.balloons()
        
    if st.button("Yeni Quiz Oluştur", type="primary"):
        start_new_quiz()
        st.rerun()
