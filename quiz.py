<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İngilizce Kelime Sınavı</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; color: #333; line-height: 1.6; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 20px; position: sticky; top: 0; background: #fff; z-index: 100;}
        .timer { font-size: 1.5em; font-weight: bold; color: #d9534f; }
        .question-block { margin-bottom: 25px; padding: 15px; border: 1px solid #e1e4e8; border-radius: 8px; background: #fafbfc; }
        .question-text { font-size: 1.2em; font-weight: bold; margin-bottom: 15px; }
        .options label { display: block; padding: 10px; margin-bottom: 8px; background: #fff; border: 1px solid #ccc; border-radius: 5px; cursor: pointer; transition: 0.2s; }
        .options label:hover { background: #e9ecef; }
        .options input[type="radio"] { margin-right: 10px; }
        button { background-color: #0056b3; color: white; border: none; padding: 12px 24px; font-size: 1.1em; border-radius: 5px; cursor: pointer; transition: 0.3s; }
        button:hover { background-color: #004494; }
        .btn-finish { background-color: #28a745; }
        .btn-finish:hover { background-color: #218838; }
        #result-screen { text-align: center; }
        .score-display { font-size: 2em; font-weight: bold; color: #0056b3; margin: 20px 0; }
    </style>
</head>
<body>

<div class="container">
    <div id="start-screen" style="text-align: center;">
        <h1>İngilizce Kelime Sınavı</h1>
        <p>Sınav <strong>90 sorudan</strong> oluşmaktadır ve süresi <strong>45 dakikadır</strong>.</p>
        <p>Sorular, yüklediğiniz defterdeki kelimelerden rastgele seçilecektir.</p>
        <button onclick="startQuiz()">Yeni Quiz Oluştur ve Başla</button>
    </div>

    <div id="quiz-screen" style="display: none;">
        <div class="header">
            <div><strong>Soru Sayısı:</strong> 90</div>
            <div class="timer" id="timer">45:00</div>
        </div>
        <div id="questions-container"></div>
        <div style="text-align: right; margin-top: 20px;">
            <button class="btn-finish" onclick="finishQuiz()">Sınavı Bitir</button>
        </div>
    </div>

    <div id="result-screen" style="display: none;">
        <h1>Sınav Bitti!</h1>
        <div class="score-display">Puanınız: <span id="score">0</span> / 90</div>
        <p>Her doğru cevap 1 puan değerindedir.</p>
        <button onclick="resetToStart()">Yeni Quiz Oluştur</button>
    </div>
</div>

<script>
    // Fotoğraflardan çıkarılan kelime havuzu
    const wordPool = [
        { en: "On time", tr: "Zamanında" }, { en: "Calm", tr: "Sakin, serin" }, { en: "Teach", tr: "Öğretmek" },
        { en: "Pen Pal", tr: "Mektup arkadaşı" }, { en: "Messy", tr: "Kirli" }, { en: "Believe", tr: "İnanmak" },
        { en: "Kind", tr: "Kibar" }, { en: "Boost", tr: "Yükseltmek" }, { en: "Plant", tr: "Bitki" },
        { en: "Patient", tr: "Hasta" }, { en: "Serious", tr: "Ciddi" }, { en: "Skill", tr: "Yetenekli" },
        { en: "Find", tr: "Bulmak" }, { en: "Foreign", tr: "Yabancı" }, { en: "Author", tr: "Yazar" },
        { en: "Express", tr: "Hızlı" }, { en: "Amount", tr: "Miktar" }, { en: "Responsibility", tr: "Sorumluluk" },
        { en: "Care", tr: "His" }, { en: "Knitting", tr: "Örgü örmek" }, { en: "Interest", tr: "İlgi, merak" },
        { en: "Idea", tr: "Fikir" }, { en: "Solve", tr: "Çözmek" }, { en: "Trouble", tr: "Problem" },
        { en: "Invent", tr: "İcat etmek" }, { en: "Spend", tr: "Para harca." }, { en: "Other", tr: "Diğeri" },
        { en: "Brain", tr: "Beyin" }, { en: "Harmony", tr: "Uyum" }, { en: "Thought", tr: "Düşünce" },
        { en: "Outgoing", tr: "Sosyal" }, { en: "Laugh", tr: "Güldürmek" }, { en: "Seems", tr: "Görünmek" },
        { en: "Ahead", tr: "İleri" }, { en: "Move", tr: "Hareket etmek" }, { en: "Confusing", tr: "Kafası karışmış" },
        { en: "Pawn", tr: "Piyon" }, { en: "Knight", tr: "Şövalye, Vezir" }, { en: "Piece", tr: "Parça" },
        { en: "Differently", tr: "Farklı" }, { en: "Mistake", tr: "Hata" }, { en: "Rush", tr: "Hızlı / Acele etmek" },
        { en: "Dangerous", tr: "Tehlikeli" }, { en: "Safe", tr: "Güvenli" }, { en: "Standing", tr: "Ayakta dur." },
        { en: "Careful", tr: "Dikkatli olmak" }, { en: "Fall", tr: "Düşmek" }, { en: "Hit", tr: "Vurmak" },
        { en: "Better", tr: "Daha iyi" }, { en: "Shore", tr: "Kıyı, sahil" }, { en: "Coast", tr: "Sahil / Kıyı" },
        { en: "Dreamy", tr: "Hayali" }, { en: "Land", tr: "Kara, toprak arazi" }, { en: "Away", tr: "Uzaklığında" },
        { en: "Hooray", tr: "Yaşasın" }, { en: "Streets", tr: "Sokak" }, { en: "Full", tr: "Dolu" },
        { en: "Road", tr: "Yol" }, { en: "Stone", tr: "Taş" }, { en: "Materials", tr: "Araç gereç" },
        { en: "Spirit", tr: "Huzurlu Ruh" }, { en: "Baker", tr: "Fırıncı" }, { en: "Decorating", tr: "Süsleme" },
        { en: "Cabinet", tr: "Raf" }, { en: "Display", tr: "Sergilemek" }, { en: "Keep", tr: "Tutmak / Bone" },
        { en: "Wear", tr: "Giyinmek" }, { en: "Smell", tr: "Koku" }, { en: "Pastry", tr: "Unlu mamüller" },
        { en: "Butcher", tr: "Kasap" }, { en: "Line", tr: "Sıra" }, { en: "Florist", tr: "Çiçekçi" },
        { en: "Field", tr: "Tarla / Alan" }, { en: "Picking", tr: "Toplanmak" }, { en: "Prepare", tr: "Hazırlamak" },
        { en: "Give up", tr: "Vazgeçmek" }, { en: "Belong", tr: "Ait olmak" }, { en: "Artwork", tr: "Sanat eseri" },
        { en: "Thirsty", tr: "Susamak" }, { en: "Each", tr: "Her biri" }, { en: "Company", tr: "Şirket" },
        { en: "Gas station", tr: "Benzinlik" }, { en: "Vitamins", tr: "Vitamin" }, { en: "Explains", tr: "Açıklamak" },
        { en: "Answer", tr: "Cevap" }, { en: "Freedom", tr: "Özgürlük" }, { en: "Sympathy", tr: "Sempati" },
        { en: "Power", tr: "Güç" }, { en: "Opinions", tr: "Fikir" }, { en: "Instructions", tr: "Klavuz vb." },
        { en: "Town square", tr: "Şehir merkezi" }, { en: "Beauty", tr: "Güzellik" }, { en: "Busy", tr: "Meşgul" },
        { en: "Knowledge", tr: "Bilgi" }, { en: "Relative", tr: "Akraba" }, { en: "Compass", tr: "Pusula" },
        { en: "Niece", tr: "Kız yeğen" }, { en: "Prefer", tr: "Tercih et." }, { en: "Living", tr: "Yaşamak" },
        { en: "Need", tr: "İhtiyaç" }, { en: "Pharmacy", tr: "Eczane" }, { en: "Still", tr: "Hala" },
        { en: "Reality", tr: "Gerçeklik" }, { en: "Escalators", tr: "Yürüyen m." }, { en: "Herbs", tr: "Bitki, baharat" },
        { en: "Pipes", tr: "Pipet" }, { en: "Piles", tr: "Yığıl" }, { en: "Means", tr: "Cimri" },
        { en: "Practice", tr: "Geliştirmek" }, { en: "Miss", tr: "Özlemek, kaçırmak, bekar" }, { en: "Tell", tr: "Anlatmak" },
        { en: "Glad", tr: "Memnun" }, { en: "Available", tr: "Müsait" }, { en: "Mayor", tr: "Belediye başkanı" },
        { en: "Relation", tr: "İlişki" }, { en: "Nephew", tr: "Erkek yeğen" }, { en: "Parent", tr: "Ebeveyn" },
        { en: "Principal", tr: "Müdür" }, { en: "Twin", tr: "İkiz" }, { en: "Leisure time", tr: "Boş zaman" },
        { en: "Novel", tr: "Roman" }, { en: "Break", tr: "Mola" }, { en: "Schedule", tr: "Program" },
        { en: "Manage", tr: "Başarmak" }, { en: "Climate change", tr: "İklim değişikliği" }, { en: "Immediate", tr: "Yakın" },
        { en: "Worst", tr: "En kötü" }, { en: "Meet", tr: "Toplantı / Buluşmak" }, { en: "Future", tr: "Gelecek" },
        { en: "Crowded", tr: "Kalabalık" }, { en: "Pavement", tr: "Kaldırım" }, { en: "Pedestrians", tr: "Yaya" },
        { en: "President", tr: "Sınıf başkanı" }, { en: "Awful", tr: "Dehşet verici" }, { en: "Lost", tr: "Kaybetmek" },
        { en: "Mean", tr: "Anlamına" }, { en: "Teammate", tr: "Takım ar." }, { en: "Spare time", tr: "Boş vakit" },
        { en: "Cool", tr: "Serin" }, { en: "Graphic", tr: "Çizgi, grafik" }, { en: "Sound", tr: "Ses" },
        { en: "Bit", tr: "Az" }, { en: "Effect", tr: "Etki" }, { en: "Share", tr: "Paylaşmak" },
        { en: "Spot", tr: "Alan" }, { en: "Get tired", tr: "Yorulmak" }, { en: "Meeting", tr: "Tanışmak" },
        { en: "Complaint", tr: "Şikayet" }, { en: "Chaos", tr: "Kaus" }, { en: "Sidewalk", tr: "Kaldırım" },
        { en: "Put", tr: "Koymak" }, { en: "Pay", tr: "Ödemek" }, { en: "ALONE", tr: "Yalnız" },
        { en: "Unfamiliar", tr: "Tanınmadık" }, { en: "To care of", tr: "İlgilenmek" }, { en: "Only", tr: "Yalnız, Tek" },
        { en: "Arrived", tr: "Ulaşmak" }, { en: "Felt", tr: "Hissetti" }, { en: "Thanks to", tr: "Sayesinde" },
        { en: "Trip", tr: "Seyehat" }, { en: "Excited", tr: "Heyecanlı" }, { en: "Upon", tr: "Üzerine" },
        { en: "Famous", tr: "Ünlü" }, { en: "Hometown", tr: "Memleket" }, { en: "Climb", tr: "Tırmanmak" },
        { en: "Return", tr: "Geri dönmek" }, { en: "Split", tr: "Bölmek" }, { en: "Worried", tr: "Endişeli" },
        { en: "Beside", tr: "Yanında" }, { en: "Just", tr: "Sadece" }, { en: "Specific", tr: "Özel" },
        { en: "Separated", tr: "Ayrılmak" }, { en: "Stomach", tr: "Karın, mide" }, { en: "Thankfully", tr: "Çok şükür" },
        { en: "Track", tr: "İzlemek" }, { en: "Case", tr: "Dava" }, { en: "Soon", tr: "Yakında" },
        { en: "Crow", tr: "Karga" }, { en: "Down", tr: "Aşağı" }, { en: "Suddenly", tr: "Birden" },
        { en: "Discover", tr: "Keşfetmek" }, { en: "Explain", tr: "Açıklamak" }, { en: "Heard", tr: "Duyulmuş" },
        { en: "Sight", tr: "Görünüş" }, { en: "Could", tr: "Olabilir" }, { en: "Comic", tr: "Komik" },
        { en: "Huge", tr: "Büyük / Devasa" }, { en: "Playwright", tr: "Oyun yaz." }, { en: "Nearly", tr: "Neredeyse" },
        { en: "Theaters", tr: "Tiyatro" }, { en: "Sign", tr: "Tabela / İşaret" }, { en: "Hang", tr: "Asmak" },
        { en: "Front", tr: "Ön" }, { en: "Waiter", tr: "Garson" }, { en: "Twist", tr: "Döndürmek" },
        { en: "Each time", tr: "Her defasında" }, { en: "Fork", tr: "Çatal" }, { en: "Another", tr: "Başka" },
        { en: "Bratwurst", tr: "Sosis" }, { en: "Pick up", tr: "Toplamak" }, { en: "Well", tr: "İyi" },
        { en: "Gift", tr: "Hediye" }, { en: "Bought", tr: "Satın almak" }, { en: "Present", tr: "Hediye" },
        { en: "Decide", tr: "Karar vermek" }, { en: "Clap", tr: "Alkışlamak" }, { en: "Seat", tr: "Oturak" },
        { en: "Wave", tr: "Dalga" }, { en: "Sell", tr: "Satmak" }, { en: "Vacation", tr: "Tatil" },
        { en: "Hang out", tr: "Takılmak" }, { en: "Jealous", tr: "Kıskanç" }, { en: "Nap", tr: "Şekerleme" },
        { en: "Happen", tr: "Olmak" }, { en: "Occur", tr: "Olmak" }, { en: "Broken", tr: "Bozuldu" },
        { en: "Informal", tr: "Gayriresmi" }, { en: "Information", tr: "Bilgi" }, { en: "Receive", tr: "Almak" },
        { en: "Imagine", tr: "Hayal et." }, { en: "Response", tr: "Cevap" }, { en: "Carefully", tr: "Dikkatlice" },
        { en: "Sender", tr: "Gönderici / Alıcı" }, { en: "Since", tr: "...'den beri" }, { en: "Pool", tr: "Havuz" },
        { en: "XOXO", tr: "Sarılıyorum ve ö." }, { en: "Reaction", tr: "Tepki" }, { en: "Snooze Button", tr: "Erteleme" },
        { en: "Nervous", tr: "Gergin, Titreşimli" }, { en: "Rude", tr: "Kaba" }, { en: "Conversation", tr: "Dialog" },
        { en: "Descriptions", tr: "Tarif" }, { en: "Appearance", tr: "Dış görünüş" }, { en: "Personality", tr: "Karakter" },
        { en: "Blond", tr: "Sarışın" }, { en: "Verb", tr: "Fiil" }, { en: "Noun", tr: "İsim" },
        { en: "Adjective", tr: "Sıfat" }, { en: "Generous", tr: "Cömert" }, { en: "Honest", tr: "Dürüst" },
        { en: "Selfish", tr: "Cimri" }, { en: "Confident", tr: "Öz güvenli" }, { en: "Live", tr: "Yaşamak" },
        { en: "Job", tr: "İş" }, { en: "Excellent", tr: "Mükemmel" }, { en: "Provide", tr: "Sağlamak" },
        { en: "Necessary", tr: "Gerekli" }, { en: "Comfortable", tr: "Konfor, rahat" }, { en: "One of", tr: "Biri" },
        { en: "Bookshop", tr: "Kitapevi" }, { en: "Grab", tr: "Almak" }, { en: "Topic", tr: "Konu" },
        { en: "Include", tr: "İçermek" }, { en: "Fiction", tr: "Kurgu" }, { en: "Host", tr: "Hizmet v." },
        { en: "Event", tr: "Davet" }, { en: "Staff", tr: "Değnek" }, { en: "Equipment", tr: "Ekipm." },
        { en: "Gather", tr: "Toplanmak" }, { en: "In conclusion", tr: "Özetle" }, { en: "Because of", tr: "Yüzünden" },
        { en: "Effort", tr: "Çaba" }, { en: "Affair", tr: "Çaba / Mesele" }, { en: "Measured", tr: "Ölçmek" },
        { en: "Similar", tr: "Benzer" }, { en: "Degree", tr: "Derece" }, { en: "Excellence", tr: "Üstünlük" },
        { en: "Most", tr: "En çok" }, { en: "Summarized", tr: "Özet" }, { en: "Sleepover", tr: "Gece kalma" },
        { en: "However", tr: "Bu şekilde / Ancak" }, { en: "Emergency", tr: "Acil durum" }, { en: "Hollow", tr: "Çukur" },
        { en: "Shell", tr: "Deniz kabuğu" }, { en: "Ancient", tr: "Eski" }, { en: "Drip", tr: "Damla" },
        { en: "Solid", tr: "Katı" }, { en: "Hole", tr: "Delik" }, { en: "Cover", tr: "Kaplamak" },
        { en: "Call", tr: "Adlandırmak" }, { en: "Visitor", tr: "Ziyaretçi" }, { en: "Tour guide", tr: "Rehber" },
        { en: "Hurt", tr: "Yaralanmak" }, { en: "Helmet", tr: "Kask" }, { en: "Crawl", tr: "Emeklemek" },
        { en: "Tight", tr: "Dar" }, { en: "Ceiling", tr: "Tavan" }, { en: "Feet", tr: "Yükseklik birimi" },
        { en: "Us", tr: "Siz, biz" }, { en: "Moss", tr: "Yosun" }, { en: "Salamander", tr: "Semender" },
        { en: "Cricket", tr: "Ateş Böceği" }, { en: "Dweller", tr: "Mağara Sakini" }, { en: "Litter", tr: "Çöp" },
        { en: "Trash", tr: "Çöp" }, { en: "Garbage", tr: "Çöp" }, { en: "Waste", tr: "Çöp" },
        { en: "Spelunker", tr: "Keşif" }, { en: "Stalactite", tr: "Sarkıt" }, { en: "Stalagmite", tr: "Dikit" },
        { en: "Lantern", tr: "Lamba" }, { en: "Reason", tr: "Sebep" }, { en: "Below", tr: "Aşağı" },
        { en: "Rock", tr: "Taş" }, { en: "Sweater", tr: "Kazak" }, { en: "Without", tr: "Sız - siz" },
        { en: "Elbow Pad", tr: "Dirseklik" }, { en: "Shine", tr: "Parlamak" }, { en: "Creak", tr: "Gıcırtı" },
        { en: "Wild life", tr: "Vahşi hayat" }, { en: "Extraordinary", tr: "Olağanüstü" }, { en: "Ordinary", tr: "Sıradan" },
        { en: "Journey", tr: "Seyahat" }, { en: "Impressive", tr: "Etkili" }, { en: "Ship", tr: "Gemi" },
        { en: "Treasure", tr: "Hazine" }, { en: "Valuable", tr: "Değerli" }, { en: "Goods", tr: "Mal" },
        { en: "Silk", tr: "İpek" }, { en: "Major", tr: "Büyük" }, { en: "Fleet", tr: "Filo" },
        { en: "Enormous", tr: "Kocaman" }, { en: "Develop", tr: "Gelişme" }, { en: "Trade", tr: "Takas" },
        { en: "Epic", tr: "Destansı" }, { en: "Expedition", tr: "Sefer" }, { en: "Reach", tr: "Ulaşmak" },
        { en: "South", tr: "Güney / Batı" }, { en: "East", tr: "Doğu" }, { en: "North", tr: "Kuzey" },
        { en: "Spread", tr: "Sürmek, yaymak" }, { en: "Establish", tr: "Kurmak" }, { en: "Tie", tr: "Bağ, ilişki, bağlar" },
        { en: "Benefited", tr: "Fayda, yarar" }, { en: "Political", tr: "Politik" }, { en: "Pole", tr: "Kutup" },
        { en: "Common", tr: "Sıradan" }, { en: "Voyage", tr: "Seyahat" }, { en: "Although", tr: "-e rağmen" },
        { en: "Death", tr: "Ölüm" }, { en: "Legacy", tr: "Efsane" }, { en: "Last", tr: "Vakit sürmek" },
        { en: "Impact", tr: "Efekt" }, { en: "Continent", tr: "Kıta" }, { en: "Global", tr: "Küresel" },
        { en: "Mark", tr: "İşaret" }, { en: "Asia", tr: "Asya" }, { en: "Europe", tr: "Avrupa" },
        { en: "Africa", tr: "Afrika" }, { en: "South America", tr: "Güney Amerika" }, { en: "North America", tr: "Kuzey Amerika" },
        { en: "Australia", tr: "Avustralya" }
    ];

    let timerInterval;
    let timeRemaining = 45 * 60; // 45 dakika (saniye cinsinden)
    let currentQuizData = [];

    function startQuiz() {
        document.getElementById("start-screen").style.display = "none";
        document.getElementById("result-screen").style.display = "none";
        document.getElementById("quiz-screen").style.display = "block";
        
        timeRemaining = 45 * 60;
        updateTimerDisplay();
        timerInterval = setInterval(countdown, 1000);
        
        generateQuestions();
    }

    function countdown() {
        timeRemaining--;
        updateTimerDisplay();
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            finishQuiz();
        }
    }

    function updateTimerDisplay() {
        let minutes = Math.floor(timeRemaining / 60);
        let seconds = timeRemaining % 60;
        document.getElementById("timer").innerText = 
            (minutes < 10 ? "0" + minutes : minutes) + ":" + 
            (seconds < 10 ? "0" + seconds : seconds);
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    function generateQuestions() {
        const container = document.getElementById("questions-container");
        container.innerHTML = "";
        currentQuizData = [];

        // Havuzu karıştır ve rastgele 90 kelime seç
        let shuffledPool = shuffleArray([...wordPool]);
        let selectedWords = shuffledPool.slice(0, 90); 

        selectedWords.forEach((wordObj, index) => {
            // 3 yanlış cevap seç
            let wrongOptions = wordPool.filter(w => w.en !== wordObj.en);
            wrongOptions = shuffleArray(wrongOptions).slice(0, 3);
            
            let options = [wordObj.tr, ...wrongOptions.map(w => w.tr)];
            options = shuffleArray(options); // Doğru şıkkın yerini rastgele yap

            currentQuizData.push({
                question: wordObj.en,
                correctAnswer: wordObj.tr
            });

            // HTML oluştur
            let qBlock = document.createElement("div");
            qBlock.className = "question-block";
            let optionsHTML = options.map((opt, i) => `
                <label>
                    <input type="radio" name="q${index}" value="${opt}">
                    ${opt}
                </label>
            `).join("");

            qBlock.innerHTML = `
                <div class="question-text">${index + 1}. "${wordObj.en}" kelimesinin Türkçe karşılığı nedir?</div>
                <div class="options">${optionsHTML}</div>
            `;
            container.appendChild(qBlock);
        });
    }

    function finishQuiz() {
        clearInterval(timerInterval);
        
        let score = 0;
        currentQuizData.forEach((data, index) => {
            let selected = document.querySelector(`input[name="q${index}"]:checked`);
            if (selected && selected.value === data.correctAnswer) {
                score++;
            }
        });

        document.getElementById("score").innerText = score;
        document.getElementById("quiz-screen").style.display = "none";
        document.getElementById("result-screen").style.display = "block";
        window.scrollTo(0, 0);
    }

    function resetToStart() {
        document.getElementById("result-screen").style.display = "none";
        document.getElementById("start-screen").style.display = "block";
    }
</script>

</body>
</html>
