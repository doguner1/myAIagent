# Local AI Toolchain for Google Antigravity

> **Amaç:** Google Antigravity'nin yerel ortamında kod tabanı hafızası,
> internet araştırması, tekrar kullanılabilir beceriler ve web işlemleri
> sağlayan; yeni GitHub araçları eklenebilen, güvenli ve bakımı kolay
> bir altyapı kurmak.
>
> **Önemli:** Bu dosya bir kurulum planı ve ajan talimatıdır. Kurulum
> yapılmadan hiçbir bileşen çalışıyor kabul edilmemelidir. Antigravity
> ajanı komutları gerçekten çalıştırmalı, test etmeli ve sonuçları
> raporlamalıdır.

## 1. Ana hedefler

1.  Google Antigravity'yi ana AI çalışma ortamı olarak kullan.
2.  Uyumlu yerel araçları öncelikle **MCP `stdio`** ile bağla. `stdio`
    kullanan araçlar için ayrı HTTP portu açma.
3.  Web arayüzü gereken uygulamaları yalnızca ihtiyaç olduğunda
    çalıştır.
4.  Birden çok HTTP arayüzü gerekiyorsa, bunları yerel ters proxy
    üzerinden tek bir giriş portunda sunmayı değerlendir. Proxy'yi sırf
    tek port hedefi uğruna ekleme.
5.  Yeni repo eklemeyi kayıt altına alınan, tekrar edilebilir bir
    prosedüre dönüştür.
6.  Sistem değişikliklerini en aza indir; kurulum, güncelleme ve
    kaldırma adımlarını belgele.
7.  Güvenlik incelemesi ve testler tamamlanmadan üçüncü taraf betikleri
    otomatik çalıştırma.

## 2. Hedef ortam ve Antigravity uyumluluğu

İşletim sistemi ve mimari önceden varsayılmamalıdır. İlk olarak
aşağıdakileri tespit et:

-   OS ve sürümü, CPU mimarisi
-   Antigravity IDE/CLI sürümü ve kullanılabilir MCP yapılandırma yolu
-   Git, Node.js, npm, Python, `uv`/pip ve Docker kullanılabilirliği
-   Mevcut MCP yapılandırmasının yedeği ve kayıtlı sunucular
-   Kullanılabilir disk alanı ve yerel port çakışmaları

Antigravity, MCP sunucularını yerel `stdio` komutlarıyla veya
`serverUrl` kullanan HTTP/SSE bağlantılarıyla yapılandırabilir.
Antigravity IDE'de yapılandırma arayüzünden **MCP Servers → Manage MCP
Servers → View raw config** yolunu kullanarak gerçek yapılandırma
dosyasını doğrula. Belgelenen yaygın konumlar:

-   IDE/global: `~/.gemini/config/mcp_config.json`
-   Workspace: `<workspace>/.agents/mcp_config.json`

Kurulumdan önce gerçek ortamda bu yolları doğrula; var olan dosyanın
üzerine yazma. Antigravity sürümüne göre arayüz ve dosya yolu
değişebileceğinden tahminle yapılandırma üretme.

Antigravity becerileri için yaygın konumlar:

-   Workspace becerileri:
    `<workspace>/.agents/skills/<skill-name>/SKILL.md`
-   Global beceriler: `~/.gemini/config/skills/<skill-name>/SKILL.md`

Yalnızca hedef uygulamanın desteklediği biçimi kullan. Claude Code'a
özel eklenti manifestlerini Antigravity'nin yerel eklentisiymiş gibi
kurma.

Resmî belgeler: - MCP: https://www.antigravity.google/docs/mcp - Skills:
https://www.antigravity.google/docs/skills - Plugins:
https://www.antigravity.google/docs/plugins

## 3. Kaynak repolar ve kurulum politikası (24 Araç)

### 3.1 `DeusData/codebase-memory-mcp`

Repo: https://github.com/DeusData/codebase-memory-mcp

**Amaç:** Kod tabanını yapısal olarak indeksleyip fonksiyonlar,
sınıflar, çağrı zincirleri ve ilişkiler üzerinden AI ajanına kod bağlamı
sunan yerel MCP sunucusu. Proje, platforma uygun çalıştırılabilir
dosyalar yayımlar; isteğe bağlı grafik arayüzü de vardır.

**Plan:** 1. Önce repo README'sinin güncel kurulum ve güvenlik
yönergelerini oku. 2. OS/mimariye uygun sürüm var mı kontrol et; indirme
adresini repo içindeki resmî sürüm bağlantısından doğrula. 3. İndirdiğin
dosyanın SHA-256 değerini yayımlanan checksum ile karşılaştır (repo
sağlıyorsa). 4. İkili dosyayı çalıştırmadan önce izinleri ve komut
seçeneklerini incele. 5. Antigravity MCP yapılandırmasına, aracın
belgelenmiş gerçek komut/argümanlarıyla `stdio` sunucusu olarak ekle. 6.
Sadece hedef proje üzerinde indeksleme yap; kullanıcı açıkça istemedikçe
tüm diski tarama. 7. Bağlantıyı Antigravity MCP panelinde doğrula ve
küçük bir test deposunda kod yapısı sorgusu yap.

Grafik arayüzü bu altyapı için zorunlu değildir. Kullanıcı özellikle
isterse aç. Repo belgeleri şu anda grafik arayüzü için `localhost:9749`
adresini belirtiyor; bunu kurulum anında yeniden doğrula. Yalnızca
`stdio` MCP sunucusu kullanılıyorsa bu arayüz portuna ihtiyaç yoktur.

### 3.2 `anthropics/claude-plugins-official`

Repo: https://github.com/anthropics/claude-plugins-official

**Amaç:** Claude Code için resmî eklenti kataloğu. Kataloğun tamamını
bir Antigravity eklentisi gibi kurma.

**Plan:** 1. Repo'yu bir **katalog ve kaynak keşif noktası** olarak
değerlendir. 2. İhtiyaç duyulan eklentinin lisansını, bakım durumunu,
kodunu ve güvenlik etkisini ayrı ayrı incele. 3. Eklentinin içindeki
becerileri Antigravity'nin açık beceri biçimine uyarlamak mümkünse
yalnızca gerekli parçaları al. 4. MCP tanımı içeriyorsa sunucunun
kendisini Antigravity'nin MCP yapılandırmasına uyarlayıp test et. 5.
Claude'a özel komutlar, hook'lar, ajan tanımları veya izinler için
otomatik uyumluluk varsayma. Uyarlama mümkün değilse nedenini raporla ve
kurma.

Bu repo doğrudan bir yerel servis değildir ve kendi başına port
açmamalıdır.

### 3.3 `rebelytics/one-skill-to-rule-them-all`

Repo: https://github.com/rebelytics/one-skill-to-rule-them-all

**Amaç:** `task-observer` adlı meta-beceri. Çok adımlı çalışma
süreçlerinde tekrarlanan örüntüleri, kullanıcı düzeltmelerini ve beceri
geliştirme fırsatlarını gözlemleyip öneriler üretir. Önerilen
değişiklikler insan incelemesinden geçmelidir.

**Plan:** 1. README, `SKILL.md`, `references/`, `scripts/`, lisans ve
kurulum yönergelerini incele. 2. Beceri klasör yapısını ve yardımcı
dosyaları koruyarak yerel Antigravity beceri dizinine kur. 3. Gerekli
etkinleştirme yönergelerini Antigravity'ye uyarlayarak ekle. Claude'a
özel yönergeleri aynen kopyalama. 4. Gözlem dosyalarının nerede
yazılacağını belirle ve bunların Git'e veya buluta yanlışlıkla
gönderilmesini engelle. 5. Yeni bir Antigravity oturumunda becerinin
algılandığını doğrula. 6. Beceriye otomatik olarak kendi talimatlarını
değiştirme izni verme; değişiklikleri önce öneri/patch olarak sunmasını
şart koş.

Port gerektirmez.

### 3.4 `goodnight000/api-anything`

Repo: https://github.com/goodnight000/api-anything

**Amaç:** Web sitelerinin kendi ağ isteklerinden tekrar kullanılabilir
işlemler öğrenen; işlemleri MCP, CLI veya TypeScript üzerinden çağırıp
JSON sonuçlar döndürebilen araç.

**Plan:** 1. Kurulumdan önce repo'nun `INSTALL.md` ve README dosyalarını
oku. 2. Projenin belirttiği Node.js sürümünü kontrol et. Güncel
README'de Node.js `22.13+` belirtiliyor; kurulum anında yeniden doğrula.
3. README'nin önerdiği kurulum yöntemini kullan. npm paketinin henüz
yayımlanmamış olabileceğini dikkate al; doğrulamadan
`npm install -g github:...` yöntemini kullanma. 4. Önce örnek, herkese
açık ve hassas olmayan bir işlemle CLI testini yap. 5. Antigravity'ye
`stdio` MCP sunucusu olarak bağla; gerçek komut ve argümanları kurulu
sürümden doğrula. 6. Site işlemi oluşturmak için gerekiyorsa tarayıcı
bağımlılığını ayrıca kur. Her kullanımda tarayıcı açılacağını varsayma.
7. Oturum açma ve çerez gerektiren işlemler için kullanıcıdan açık izin
al; parolaları veya çerezleri README'ye, kaynak koduna ya da loglara
yazma. 8. Üçüncü taraf sitelerin hizmet koşullarına, erişim
kontrollerine ve hız sınırlamalarına uy.

MCP `stdio` modunda port gerektirmez. Aracın dahili HTTP işlevi, merkezi
bir web portu ile aynı şey değildir.

### 3.5 `Panniantong/agent-reach`

Repo: https://github.com/Panniantong/agent-reach

**Amaç:** AI ajanının web sayfaları, YouTube, RSS, GitHub ve
yapılandırıldığında çeşitli sosyal platformlar gibi kaynaklardan bilgi
alabilmesi için CLI tabanlı yetenek katmanı. Her kanal aynı erişim
düzeyini sağlamaz; bazıları oturum, çerez veya ek araç ister.

**Plan:** 1. Repo'daki güncel kurulum kılavuzunu, güvenlik politikasını
ve lisansı oku. 2. Önce salt kontrol/dry-run yöntemini kullan; hangi
komutların kurulacağını ve hangi yapılandırmaların değişeceğini raporla.
3. Varsayılan `agent-reach install` davranışının sistem değişikliği
yapmayabileceğini dikkate al. `--system` gibi sistem çapında değişiklik
yapan seçenekleri kullanıcı açıkça onaylamadan çalıştırma. 4. Güncel
kurulum kılavuzuna göre doğru Python paketleme yöntemini kullan;
PyPI'daki aynı adlı farklı paketi yanlışlıkla kurma. 5. Antigravity'nin
shell/skill yeteneklerine uyarlamak için repo'nun güncel skill
yönergelerini kullan. CLI'nin Antigravity'de doğrudan MCP sunucusu gibi
çalıştığını varsayma. 6. Kurulum sonrası `agent-reach doctor` çalıştır;
her kanalın durumunu raporla. 7. Önce giriş gerektirmeyen kanalları test
et. Sosyal hesapları, çerezleri ve tokenları yalnızca kullanıcı seçerse
yapılandır. 8. Kimlik bilgilerini yerel, erişimi kısıtlı yapılandırmada
tut. Çerez ve tokenları loglama veya başka servislere gönderme.

Çoğu işlev CLI/skill aracılığıyla çalışır; varsayılan olarak web portu
gerektirmez. Platform erişimleri değişebilir, bu nedenle `doctor` sonucu
gerçek durumun kaynağıdır.

### 3.6 `ItzCrazyKns/Vane`

Repo: https://github.com/ItzCrazyKns/Vane

**Amaç:** Kendi bilgisayarında çalıştırılabilen AI destekli arama ve
cevap motoru. Diğer araçlardan farklı olarak esasen kullanıcıya yönelik
bir web arayüzü sunar.

**Plan:** 1. README ve Docker yönergelerini incele; Docker kurulu
değilse yalnızca Vane için otomatik olarak Docker yükleme. 2.
Başlangıçta isteğe bağlı bileşen olarak bırak. MCP/CLI üzerinden aynı
araştırma ihtiyacı zaten karşılanıyorsa ilk kurulumda Vane'i çalıştırmak
zorunlu değildir. 3. Kullanıcı web arayüzünü isterse resmi Docker
yönergesini kullan, imaj adını ve değişkenleri güncel repo'dan doğrula.
4. Kalıcı veriler için belgelenen volume kullanımını koru. 5. Varsayılan
arayüz portunun güncel dokümanda `3000` olduğunu doğrula; yalnızca
`127.0.0.1` üzerinden erişilebilir olmasını tercih et. 6. Slim sürüm
SearXNG gibi harici arama altyapısı gerektiriyorsa bunu ayrıca belirt;
SearXNG adresini varsayma. 7. Vane'i tek port girişine eklemek gerekirse
yalnızca localhost'a bağlı bir reverse proxy tasarla. Proxy arkasında
çalıştığı doğrulanmadan portları kapatma. 8. İnternete açık bind
(`0.0.0.0`) veya router port yönlendirmesi oluşturma.

Vane ilk aşamada isteğe bağlıdır; tüm araçlar için ortak port yaratmanın
gerekçesi değildir.

### 3.7 `msitarzewski/agency-agents`

Repo: https://github.com/msitarzewski/agency-agents

**Amaç:** Mühendislik, tasarım, ürün, satış, pazarlama ve strateji gibi
farklı disiplinlerde uzmanlaşmış onlarca yapay zeka ajanı ve rol tanımından
oluşan modüler ajans kadrosu ("The Agency"). Her ajan kendine özgü bir
uzmanlık, çalışma yöntemi, iletişim dili ve somut teslimat (deliverables)
standartlarına sahiptir.

**Plan:** 1. Repo'yu doğrudan çalıştırılabilir bir servis değil, **uzman
ajan/rol ve beceri kataloğu** olarak değerlendir. 2. Kataloğun tamamını tek
seferde körlemesine sisteme yükleme; yalnızca çalışma sürecinde ihtiyaç
duyulan bölümleri (Divisions: Engineering, Design vb.) seç. 3. Antigravity
entegrasyonu için projenin dönüştürme ve kurulum betiklerini incele
(`scripts/convert.sh` ve `./scripts/install.sh --tool antigravity`). 4. Seçilen
ajanları Antigravity'nin standart Subagent (`agents/`) veya Skill
(`<workspace>/.agents/skills/` ya da `~/.gemini/config/skills/`) yapısına
aktar; Claude/Cursor'a özel komutları ve hook'ları Antigravity biçimine
uyarla. 5. Ajan tanımlarının salt yönlendirici persona/kılavuz olduğunu,
sisteme kontrolsüz kabuk (shell) veya dosya silme yetkisi vermediğini doğrula.
6. Seçilen rollerin Antigravity oturumunda doğru bağlam ve çıktılar ürettiğini
test et.

Port gerektirmez; dosya tabanlı kural ve ajan kataloğudur.

### 3.8 `JuliusBrussee/caveman`

Repo: https://github.com/JuliusBrussee/caveman

**Amaç:** Kodlama ajanlarının yanıtlarındaki gereksiz selamlama, gevezelik ve
tekrarı ortadan kaldırarak token kullanımını ve maliyeti %33 ile %65 oranında
azaltan, bağımsız araştırmalarla (Adobe Research, JetBrains, Elastic Labs)
doğrulanmış özlü yanıt ve girdi optimizasyon aracı (Skill + Proxy).

**Plan:** 1. Aracı iki kademeli olarak değerlendir: **Küçük Taş (Skill)** ve
**Büyük Taş (Proxy)**. 2. **İlk olarak Skill katmanını entegre et:**
Antigravity için `/caveman` formatını (ASD-STE100 kontrollü dil ilkeleri:
aktif fiil, tek cümle kuralı, gereksiz nezaket yok; ancak kod blokları, dosya
yolları, hata mesajları ve güvenlik uyarıları harfi harfine korunur) yerel bir
Antigravity becerisi olarak tanımla. 3. Skill'i `npx skills add JuliusBrussee/caveman -g`
ile veya yerel `SKILL.md` yönergesi olarak sisteme dahil et. 4. **Proxy
katmanını (The Proxy)** opsiyonel değerlendir: Sistemde Node.js `22.13+`
sürümünü doğrula; ajan oturumlarında devasa log, CSV, JSON veya test çıktıları
okunacaksa `caveman` CLI sıkıştırma komutlarını (`caveman shrink`, `caveman browse`)
test et. 5. Telemetri politikasını kontrol et; dışarıya kullanım verisi
gitmemesi için `caveman telemetry off` veya `DO_NOT_TRACK=1` ortam değişkenini
zorunlu kıl. 6. Kod ve veri bütünlüğü testi yap: Caveman modunun kod bloklarını
ve diff'leri eksiltmediğini, sadece açıklayıcı metinleri kısalttığını doğrula.

Skill modu port gerektirmez; Proxy modu yerel ara süreçtir ve dış ağa port
açmaz.

### 3.9 `akitaonrails/ai-memory`

Repo: https://github.com/akitaonrails/ai-memory

**Amaç:** AI kodlama ajanları için oturumlar ve araçlar arası uzun vadeli epizodik ve anlamsal hafıza. Ajanın mimari kararları, kota döngülerini, başarısız denemeleri ve kullanıcı tercihlerini unutmadan sonraki oturumlara aktarmasını sağlar.

**Plan:** 1. `install.sh` veya derlenmiş Rust ikilisi ile yerel ikiliyi incele. 2. `ai-memory setup --yes --agent antigravity-cli` ile entegrasyonu sağla. 3. Proje bazlı `pending_pool.json`, YouTube kota pencereleri ve mimari kısıtları kalıcı hafıza şemasına kaydet. 4. Port gerektirmez; `agent-longterm-memory` becerisi olarak Antigravity skill dizinine entegre edilmiştir.

### 3.10 `666ghj/MiroFish`

Repo: https://github.com/666ghj/MiroFish

**Amaç:** Sürü zekası (Swarm Intelligence) simülasyon motoru. Çoklu sentetik izleyici/kullanıcı personaları yaratarak içeriklerin virallik potansiyelini, izleyici tepkilerini ve kamuoyu eğilimlerini tahmin eder.

**Plan:** 1. Doğukan ve Pixlabss otonom keşif ajanlarına virallik stres-testi katmanı olarak ekle. 2. Kurgulanan kanca (hook), başlık ve sabit yorumları sentetik kitle personaları üzerinde simüle et. 3. İzleyiciyi yorum yapmaya kışkırtan veya tartışma başlatan dinamikleri otomatik puanla. 4. Port gerektirmez; `swarm-trend-predictor` becerisi olarak yapılandırılmıştır.

### 3.11 `Automattic/harper`

Repo: https://github.com/Automattic/harper

**Amaç:** Automattic tarafından geliştirilen çevrimdışı, gizlilik odaklı, ultra-hızlı Rust tabanlı dilbilgisi, diksiyon ve üslup denetleyicisi.

**Plan:** 1. Seslendirme metinlerinde yapay zeka tokenlaştırıcılarını şaşırtan ham rakamları, garip noktalama işaretlerini ve telaffuz tuzaklarını tespit et. 2. Pixlabss ve Doğukan altyazı senkronizasyonunda (ASS formatı) 1.5–2.5 saniyelik görsel okuma pencerelerini ve satır bölünmelerini denetle. 3. `offline-grammar-checker` becerisi olarak sisteme dahil edilmiştir.

### 3.12 `mattpocock/skills`

Repo: https://github.com/mattpocock/skills

**Amaç:** Total TypeScript yazarı Matt Pocock'un gerçek mühendisler için hazırladığı; Wayfinder kod tabanı navigasyonu, strict domain modelleme, spec-to-code disiplini ve ajan prompt mühendisliğini birleştiren çekirdek beceri paketi.

**Plan:** 1. `wayfinder`, `domain-modeling`, `implement-spec`, `diagnosing-bugs` ve `writing-for-agents` pratiklerini Antigravity standartlarına aktar. 2. Kod yazmadan önce modül sınırlarını ve tipleri doğrula; gereksiz soyutlama ve kod şişkinliğini önle. 3. `engineer-core-skills` becerisi olarak entegre edilmiştir.

### 3.13 `BitterSecurity/Decepticon`

Repo: https://github.com/BitterSecurity/Decepticon

**Amaç:** Otonom Kırmızı Takım (Red Team) sızma testi, saldırı yüzeyi haritalama ve güvenlik açığı keşif ajanı.

**Plan:** 1. Guner AV (antivirüs) projesinde zararlı yazılım tespiti, saldırı vektörleri ve savunma atlatma tekniklerini test etmek için kullan. 2. iOS jailbreak (iPhone 7 / Dopamine 2 rootless) ortamında SSH servislerini (`root@192.168.1.103:2222`), sandbox sınırlarını ve izin hiyerarşisini denetle. 3. `autonomous-redteam-pentest` becerisi olarak yapılandırılmıştır.

### 3.14 `NationalSecurityAgency/ghidra`

Repo: https://github.com/NationalSecurityAgency/ghidra

**Amaç:** NSA tarafından geliştirilen amiral gemisi Yazılım Tersine Mühendislik (SRE) çatısı: decompiler, disassembler, ARM64 Mach-O/ELF ikili analizi.

**Plan:** 1. iPhone 7 (iOS 15.8.x Dopamine 2) üzerinde SpringBoard ve sistem kütüphanelerini decompile ederek rootless tweak geliştirmek için gerekli Objective-C selector'larını, C fonksiyon offset'lerini ve kanca (hook) noktalarını tespit et. 2. Guner AV projesinde şüpheli ikili dosyaları decompile ederek imza analizi yap. 3. `ghidra-reverse-engineering` becerisi olarak entegre edilmiştir.

### 3.15 `lyogavin/airllm`

Repo: https://github.com/lyogavin/airllm

**Amaç:** Katman katman (layer-by-layer) bellek akışı mimarisiyle, tek bir 4GB GPU veya Mac CPU üzerinde devasa LLM'leri (70B, 125B, 2.8T) kuantizasyon kaybı olmadan sıfır maliyetle yerelde çalıştırma.

**Plan:** 1. Projenin "para kazanana kadar sıfır maliyetle çalış" felsefesine uygun olarak, gelecekteki çevrimdışı ağır analiz görevlerini (uzun transkript özetleme, toplu içerik madenciliği) API ücreti ödemeden yerelde yürütmek için mimari şablon olarak konumlandır. 2. `airllm-zero-cost-inference` becerisi olarak sisteme kaydedilmiştir.

### 3.16 `apache/maka`

Repo: https://github.com/apache/maka

**Amaç:** Otonom ajanların gerçekleştirdiği tüm araç çağrılarını, durum geçişlerini ve kararları olay tabanlı (event-sourced) ve değiştirilemez şekilde kaydeden yüksek performanslı ajan çalışma alanı.

**Plan:** 1. GitHub Actions üzerinde çalışan otonom üretim boru hatlarında (`upload_receipts.json`, `pending_pool.json`, `latest_plan.json`) eksiksiz izlenebilirlik sağla. 2. Kota aşımlarında veya hata anlarında adli tıp analizi yaparak bir sonraki döngüye sıfır veri kaybıyla geçişi güvenceye al. 3. `agent-audit-trail` becerisi olarak yapılandırılmıştır.

### 3.17 `MadsLorentzen/ai-job-search`

Repo: https://github.com/MadsLorentzen/ai-job-search

**Amaç:** Yerel çalışan otonom kariyer ve teknik yetkinlik analiz motoru; projelerden ve kod tabanlarından somut teknik portföy sentezleme.

**Plan:** 1. Geliştirilen otonom fabrikaların, güvenlik araçlarının ve iOS tweak projelerinin teknik yetkinliklerini analiz edip somut başarı kanıtlarına dönüştür. 2. `career-profile-synthesizer` becerisi olarak eklenmiştir.

### 3.18 `morluto/rea`

Repo: https://github.com/morluto/rea

**Amaç:** Reverse Engineer Anything (REA). İkili dosyalardan (Mach-O, ELF, PE) masaüstü ve Electron uygulamalarına kadar her katmanda çalışan, 207 MCP aracı ve CLI içeren otonom tersine mühendislik çatısı.

**Plan:** 1. `npm install -g rea-agents` ile küresel CLI ve MCP sunucusunu doğrula (`/opt/homebrew/bin/rea-agents`, v6.5.0). 2. `~/.gemini/config/mcp_config.json` dosyasına `rea` stdio MCP sunucusu olarak ekle. 3. `rea-reverse-engineer` becerisi olarak Antigravity skill dizinine entegre et. 4. Port gerektirmez; yerel MCP `stdio` ve CLI üzerinden çalışır.

### 3.19 `desktop/desktop`

Repo: https://github.com/desktop/desktop

**Amaç:** GitHub Desktop açık kaynak mimarisi ve modern Electron/Masaüstü uygulamalarının derinlemesine tersine mühendisliği, `.asar` paketlerinin açılması, IPC iletişim denetimi ve temiz oda (clean-room) mantık rekonstrüksiyonu.

**Plan:** 1. `@electron/asar` ikilisi ile macOS ve Electron uygulamalarının paket analizini sağla (`/opt/homebrew/bin/asar`, v4.3.1). 2. Masaüstü UI/UX tersine mühendisliği ve Guner AV güvenlik denetimlerinde Electron zafiyet taraması için kılavuzlaştır. 3. `desktop-app-reverse-engineering` becerisi olarak Antigravity skill dizinine entegre et. 4. Port gerektirmez.

### 3.20 `evolution-foundation/evolution-api`

Repo: https://github.com/evolution-foundation/evolution-api

**Amaç:** Açık kaynak REST tabanlı çok kanallı mesajlaşma ve WhatsApp ağ geçidi. Baileys (WhatsApp Web Multi-Device) ve Resmi Meta WhatsApp Cloud API desteği; Typebot, Chatwoot, Dify, OpenAI, RabbitMQ, Kafka, SQS ve webhook entegrasyonları ile ajanların WhatsApp ve mesajlaşma kanalları üzerinden harici dünyayla iletişim kurmasını sağlama.

**Plan:** 1. `evolution-api-gateway` becerisi olarak Antigravity skill dizinine (`~/.gemini/config/skills/evolution-api-gateway/`) entegre et. 2. İhtiyaç duyulduğunda Docker (`atendai/evolution-api:v2.3.7`) veya Node.js ile yerel `localhost:8080` portunda izole çalıştır. 3. Global API Key (`AUTHENTICATION_API_KEY`) ve webhook imzalama zorunluluğu getir. 4. Portsuz çalışma kuralı gereğince yalnızca mesajlaşma/otomasyon tetiklendiğinde ayağa kaldır.

### 3.21 `every-app/open-seo`

Repo: https://github.com/every-app/open-seo

**Amaç:** Semrush ve Ahrefs'e açık kaynak, kullandıkça öde (pay-as-you-go) alternatifi. Anahtar kelime araştırması, sıralama takibi (rank tracking), rakip analizi, backlink denetimi, teknik site denetimleri ve LLM yanıtlarında marka görünürlüğü takibi (AI Visibility / GEO).

**Plan:** 1. `openseo-intelligence` becerisi olarak Antigravity skill dizinine (`~/.gemini/config/skills/openseo-intelligence/`) entegre et. 2. OpenSEO MCP sunucusu ve DataForSEO API katmanıyla ajanların doğrudan SEO sorguları, SERP analizleri ve site denetimleri yapmasını sağla. 3. İsteğe bağlı olarak Docker (`localhost:3000`) veya Cloudflare Workers üzerinden portsuz/dağıtık barındırma desteği sağla.

### 3.22 `obra/superpowers`

Repo: https://github.com/obra/superpowers

**Amaç:** Kodlama ajanları için eksiksiz yazılım geliştirme metodolojisi ve birleştirilebilir beceri çerçevesi. Spek netleştirme, beyin fırtınası, kırmızı/yeşil TDD (Test-Driven Development), alt-ajan koordinasyonu ve kanıta dayalı tamamlama doğrulaması.

**Plan:** 1. `superpowers-methodology` becerisi olarak Antigravity skill dizinine (`~/.gemini/config/skills/superpowers-methodology/`) entegre et. 2. Ajanların plansız kod yazmasını engelleyen `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development` ve `verification-before-completion` disiplinlerini aktif kıl. 3. Port ve ek dış servis gerektirmez; tamamen kural ve iş akışı tabanlıdır.

### 3.23 `darkzOGx/youtube-automation-agent`

Repo: https://github.com/darkzOGx/youtube-automation-agent

**Amaç:** Kendi makinenizde çalışan, baştan sona bir YouTube kanalını yöneten açık kaynaklı otonom AI ajanı. Trend araştırması, senaryo yazımı, seslendirme (TTS), görsel ve video üretimi (MP4 derleme), meta veri SEO optimizasyonu ve insan onaylı zamanlanmış yayınlama.

**Plan:** 1. `youtube-automation-agent` becerisi olarak Antigravity skill dizinine (`~/.gemini/config/skills/youtube-automation-agent/`) entegre et. 2. YouTube Shorts ve video prodüksiyon iş akışlarında yerel FFmpeg/Node derleme altyapısıyla çalıştır. 3. İnsan onay kapısı (Human-in-the-loop) sayesinde nihai onay olmadan doğrudan video yüklemeyi engelle. 4. Portsuz yerel CLI/betik moduyla çalıştır; gerekirse yerel operatör paneli üzerinden yönet.

### 3.24 `kalil0321/reverse-api-engineer`

Repo: https://github.com/kalil0321/reverse-api-engineer

**Amaç:** Herhangi bir web sitesinin özel HTTP ağ trafiğini tarayıcı üzerinden (HAR formatında) dinleyerek Python, TypeScript, Go, Java vb. dillerde güçlü tipli (typed) API istemcisine dönüştüren otonom tersine mühendislik aracı.

**Plan:** 1. `reverse-api-engineer` becerisi olarak Antigravity skill dizinine (`~/.gemini/config/skills/reverse-api-engineer/`) entegre et. 2. `repos/reverse-api-engineer` üzerinden yerel kaynak kodunu koru. 3. Ajanların harici API'si olmayan web sitelerine programatik erişim istemcisi yazması gerektiğinde CLI/ajan moduyla çalıştır. 4. Port gerektirmez.

## 4. Önerilen mimari

### İlk aşama: mümkün olduğunca portsuz

-   **Antigravity:** Ana ajan.
-   **codebase-memory-mcp:** Yerel MCP `stdio`.
-   **API Anything:** Yerel MCP `stdio`.
-   **REA (Reverse Engineer Anything):** Yerel MCP `stdio` (207 araç) + CLI.
-   **task-observer:** Yerel skill klasörü.
-   **Agent Reach:** CLI + Antigravity skill/yönergesi; uyumluluğu test ederek.
-   **Agency Agents:** Uzmanlık/rol ve beceri kataloğu.
-   **Caveman:** Token optimizasyonu ve özlü yanıt katmanı.
-   **ai-memory:** Uzun vadeli epizodik ajan hafızası.
-   **MiroFish (Swarm Trend Predictor):** Çoklu ajan virallik ve kitle reaksiyon simülasyonu.
-   **Harper (Offline Grammar):** Rust tabanlı diksiyon, fonetik ve altyazı linter'ı.
-   **Matt Pocock Skills:** Wayfinder kod navigasyonu ve strict domain modelleme.
-   **Decepticon:** Otonom kırmızı takım sızma testi ve Guner AV güvenlik denetimleri.
-   **Ghidra:** ARM64 Mach-O tersine mühendislik ve iOS Dopamine tweak hook analizi.
-   **Desktop App Reversing:** Electron/React ASAR açma, IPC denetimi ve temiz oda mimari çıkarma.
-   **Evolution API:** Çok kanallı WhatsApp ve mesajlaşma ağ geçidi; ihtiyaç anında Docker/API üzerinden çağrılan mesajlaşma motoru.
-   **OpenSEO:** Açık kaynak SEO, rakip analizi ve AI arama görünürlüğü motoru; yerel MCP ve DataForSEO entegrasyonu.
-   **Superpowers:** Ajanik yazılım geliştirme metodolojisi, spec netleştirme, alt-ajan koordinasyonu ve kanıt odaklı TDD disiplini.
-   **YouTube Automation Agent:** Uçtan uca otonom YouTube video ve Shorts fabrikası; araştırma, senaryo, ses, görsel, montaj ve onaylı yayınlama.
-   **Reverse API Engineer:** Web sitelerinin özel ağ trafiğini (HAR) otomatik tip güvenli API istemcilerine dönüştüren CLI/Ajan aracı.
-   **AirLLM:** Sıfır maliyetli katman katman yerel LLM akıl yürütme.
-   **Apache Maka:** Olay tabanlı izlenebilirlik ve denetim izi.
-   **Claude Plugins Official:** Seçili bileşenler için katalog; toplu kurulum yok.
-   **Vane:** Kullanıcı web arayüzü istiyorsa isteğe bağlı Docker servisi.

### Tek web portu ne zaman gerekli?

MCP `stdio` süreçleri bir TCP portu kullanmadığından bunları tek HTTP
portunda toplamak gerekli değildir. Vane gibi web uygulamaları kendi
portunu kullanabilir. Birden fazla web arayüzü gerçekten gerekiyorsa şu
yaklaşımı değerlendir:

`Tarayıcı → localhost:8080 (reverse proxy) → Vane ve diğer yerel web servisleri`

Bu bir tasarım hedefidir; proxy kurulumunu ilk aşamada yapma. Önce
Vane'in gerçekten gerekli olduğunu doğrula. Proxy eklenirse: - yalnızca
loopback arayüzüne bağla; - yalnızca gereken yolları yönlendir; -
yönetim uçlarını internete açma; - WebSocket ve uygulama taban yolu
gereksinimlerini test et; - doğrudan servis portlarının yerel erişim
politikasını bozma; - proxy çalışıyor diye arka servis portlarını
körlemesine kapatma.

## 5. Kurulum öncesi güvenlik kuralları

Aşağıdaki kurallar zorunludur:

1.  **Önce incele, sonra çalıştır.** `curl ... | bash`, `irm ... | iex`
    veya benzeri uzaktan kod yürütme kalıplarını kaynağı incelemeden
    çalıştırma.
2.  GitHub reposunun sahibi, lisansı, son etkinliği, sürümleri ve
    güvenlik uyarılarını kontrol et.
3.  Mümkünse sabit release/commit kullan; `main`/`latest`
    güncellemelerinin değişebilir olduğunu kaydet.
4.  Mevcut Antigravity MCP yapılandırmasını yedekle. JSON'u programatik
    olarak birleştir; var olan girdileri silme.
5.  Mevcut dosya ve ayarlara dokunmadan önce değişiklik planını göster.
6.  Parola, API key, OAuth secret ve çerezleri repoya veya README'ye
    yazma.
7.  Yıkıcı komutlar, `sudo`, sistem paketi kurulumu, güvenlik ayarlarını
    değiştirme, toplu dosya silme ve kullanıcı hesabı/oturumuna erişim
    için önce onay al.
8.  Sosyal platform çerezlerinin hesap erişimi anlamına geldiğini
    varsay; kullanıcı açıkça seçmeden içe aktarma.
9.  Lisansı ve kullanım koşullarını kontrol et; erişim kısıtlamalarını
    aşmaya çalışma.
10. Testler başarısızsa "kuruldu ve çalışıyor" deme.
11. Loglarda gizli değerleri maskele.
12. Başarısız kurulumda geri alma yöntemini uygula; kullanıcı verisini
    veya mevcut MCP yapılandırmasını silme.

## 6. Ajanın uygulayacağı kurulum aşamaları

### Aşama A --- Keşif ve rapor

1.  OS, mimari, Antigravity sürümü ve araçları tespit et.
2.  MCP yapılandırma dosyasını bul ve yedekle.
3.  Altı repo'nun README, lisans, release ve kurulum yönergelerini
    güncel kaynaklardan oku.
4.  Her araç için `uyumlu`, `uyarlama gerekli`, `isteğe bağlı` veya
    `engelli` kararı ver.
5.  Bağımlılıkları ve olası portları raporla.
6.  Kullanıcı onayı gerektiren adımları listele.

### Aşama B --- Minimum güvenli kurulum

1.  `codebase-memory-mcp` için doğrulanmış kurulum yöntemini kullan.
2.  `api-anything` için doğru Node sürümünü ve repo'nun önerdiği
    paketleme yöntemini kullan.
3.  `task-observer` dosyalarını eksiksiz bir skill klasörüne kur ve
    Antigravity'ye uyumlu yönergeleri hazırla.
4.  `agent-reach` için önce dry-run/doctor ve salt kontrol uygula;
    sistem değişikliklerini onay olmadan yapma.
5.  Claude eklenti deposunu yalnızca inceleme/katalog amaçlı kullan;
    seçilmiş ve uyarlanabilir bir bileşen yoksa kurulum yapma.
6.  Vane'i kullanıcı arayüzü gereksinimi doğrulanana kadar kurma.
7.  Tüm indirme ve kurulum adımlarını kaydet.

### Aşama C --- MCP yapılandırması

Önce mevcut dosyayı yedekle. Her sunucunun gerçek komut yolunu,
argümanlarını ve gerekiyorsa `cwd`/`env` değerlerini kurulumdan sonra
doğrula. Aşağıdaki örnek yalnızca şema örneğidir; doğrulanmamış komut
yollarını aynen kullanma:

``` json
{
  "mcpServers": {
    "example-local-tool": {
      "command": "/absolute/path/to/verified-command",
      "args": [],
      "disabled": false
    }
  }
}
```

Kurulu her MCP sunucusu için: - `command` gerçekten var mı? - `args`
güncel README ile eşleşiyor mu? - Gizli anahtar gerekiyor mu? - `stdio`
üzerinden başlatılabiliyor mu? - Antigravity MCP panelinde bağlantı
kuruluyor mu? - Araç listesi ve en az bir salt-okunur test başarılı mı?

MCP JSON'unda yorum ekleme. Yapılandırmayı yazdıktan sonra JSON parse
testi yap. Var olan sunucu tanımlarını koru. Gerçek dosya yolu farklıysa
yukarıdaki örneği değil, bulunan yolu kullan.

### Aşama D --- Beceri entegrasyonu

1.  Antigravity'nin skill konumunu doğrula.
2.  Her skill için ayrı klasör oluştur; repo içeriğini tek bir
    `SKILL.md` içine gelişigüzel birleştirme.
3.  `task-observer` için gerekli `references/` ve `scripts/` dosyalarını
    koru.
4.  Skill açıklamalarını Antigravity'nin algılayacağı kadar açık yaz.
5.  Skill'in sistemde hangi dosyaları yazabileceğini ve nasıl
    etkinleştiğini belgele.
6.  Yeni oturumda beceriyi test et.

### Aşama E --- Test ve kabul ölçütleri

Aşağıdakiler kanıtlanmadan işi tamamlandı sayma:

-   [ ] OS ve mimari doğru tespit edildi.
-   [ ] Önceki MCP yapılandırmasının yedeği var.
-   [ ] MCP JSON geçerli.
-   [ ] codebase-memory-mcp Antigravity'de bağlı ve örnek kod sorgusu
    başarılı.
-   [ ] API Anything CLI testi başarılı ve MCP bağlantısı doğrulandı.
-   [ ] task-observer becerisi Antigravity'de algılanıyor.
-   [ ] Agent Reach `doctor` raporu kaydedildi; desteklenmeyen kanallar
    açıkça belirtildi.
-   [ ] Claude eklentileri Antigravity uyumlu diye yanlışlıkla topluca
    kurulmadı.
-   [ ] Agency Agents içinden seçilen roller Antigravity skill/subagent formatında sorunsuz algılanıyor.
-   [ ] Caveman skill kuralı test edildi; kod blokları eksiksiz, metinler özlü ve telemetri kapalı.
-   [ ] Vane kurulmuşsa arayüz yalnızca yerel makineden erişilebiliyor.
-   [ ] Gereksiz port açılmadı.
-   [ ] Gizli değerler loglara veya depoya yazılmadı.
-   [ ] Kurulum, güncelleme ve kaldırma yönergeleri kaydedildi.

## 7. Yeni repo ekleme protokolü

Kullanıcı yeni bir GitHub URL'si verdiğinde şu akışı uygula:

1.  URL'yi doğrula ve repo'nun gerçek sahibini kontrol et.
2.  README, lisans, release, bağımlılık, kurulum betikleri ve güvenlik
    politikasını incele.
3.  Aracın türünü sınıflandır:
    -   MCP `stdio`
    -   MCP HTTP/SSE
    -   CLI
    -   Antigravity skill
    -   web uygulaması
    -   Claude'a özgü plugin
    -   başka/uyarlama gerektiren
4.  Var olan araçlarla işlev çakışmasını belirle.
5.  Port, RAM, CPU, disk, Docker ve dış servis ihtiyacını belirle.
6.  Riskleri ve yapacağı dosya değişikliklerini kullanıcıya açıkla.
7.  Önce dry-run veya güvenli test yap.
8.  Kurulumu yalnızca gerekli izinlerle yap.
9.  Antigravity entegrasyonunu ve işlev testini doğrula.
10. `TOOL-CATALOG.md` dosyasına kayıt ekle.
11. Başarısızsa sebebi, log konumu ve güvenli geri alma yolunu kaydet.

### Araç kataloğu şablonu

Her yeni araç için şu alanları doldur:

  Alan                İçerik
  ------------------- -------------------------------------------------------
  Repo URL            Kanonik GitHub bağlantısı
  Amaç                Tek cümlelik açıklama
  Durum               Aday / incelendi / kuruldu / test edildi / devre dışı
  Entegrasyon türü    MCP stdio / MCP HTTP / CLI / Skill / Web
  Sürüm veya commit   Kurulu sürümün sabit kimliği
  Bağımlılıklar       Node, Python, Docker vb.
  Port                Yok veya doğrulanmış localhost portu
  Yapılandırma        Eklenen dosyalar; gizli değerler olmadan
  Test kanıtı         Komut, sonuç ve tarih
  Güvenlik notu       İzinler, token/çerez ve riskler
  Kaldırma            Veri koruyan kaldırma adımları

## 8. Önerilen klasör yapısı

Bu klasör yapısı bir hedef önerisidir. Önce mevcut workspace'i incele;
var olan projelerin üstüne yazma.

``` text
local-ai-toolchain/
├── README.md
├── TOOL-CATALOG.md
├── docs/
│   ├── INSTALL-REPORT.md
│   ├── SECURITY.md
│   └── TROUBLESHOOTING.md
├── backups/
│   └── (MCP yapılandırma yedekleri; Git'e eklenmez)
├── repos/
│   ├── codebase-memory-mcp/
│   ├── claude-plugins-official/
│   ├── one-skill-to-rule-them-all/
│   ├── api-anything/
│   ├── agent-reach/
│   ├── agency-agents/
│   ├── caveman/
│   └── Vane/
└── .gitignore
```

Repo klonları yalnızca gerçekten kaynak incelemek veya yerel dosyalara
ihtiyaç varsa oluşturulsun. Kurulu bir ikili/CLI yeterliyse yalnızca
sırf klasör yapısı dolsun diye kaynak kodu klonlama. `backups/`,
tokenlar, çerezler, `.env` dosyaları ve özel indeks verileri sürüm
kontrolüne eklenmemelidir.

## 9. Güncelleme, geri alma ve kaldırma

-   Güncellemeden önce mevcut sürüm, yapılandırma ve test sonucunu
    kaydet.
-   Her repo için upstream güncelleme talimatını uygula; bütün araçları
    tek komutla körlemesine güncelleme.
-   Önce test ortamında veya örnek projede doğrula.
-   Güncelleme başarısızsa son çalışan sürüme dönme yolunu belgele.
-   Kaldırırken yalnızca bu kurulumun oluşturduğu dosya ve yapılandırma
    girdilerini kaldır.
-   İndeksleri, kullanıcı verilerini, Vane volume'lerini ve başka
    araçların MCP girdilerini açık kullanıcı onayı olmadan silme.
-   Bir araç kaldırıldığında Antigravity yapılandırmasındaki yalnızca o
    araca ait girdiyi çıkar; JSON'un kalanını koru.

## 10. Son rapor formatı

Kurulum sonunda şu başlıklarla `docs/INSTALL-REPORT.md` oluştur:

1.  Sistem tespiti (OS, mimari, Antigravity sürümü)
2.  Kurulan ve kurulmayan araçlar
3.  Her araç için kurulu sürüm/commit ve entegrasyon türü
4.  MCP bağlantı testi ve kullanılan doğrulama komutları
5.  Skill algılama testi
6.  Açık portlar ve bunların nedenleri
7.  Güvenlik incelemesi ve alınan izinler
8.  Başarısız testler ve bilinen sınırlamalar
9.  Geri alma/kaldırma yönergeleri
10. Yeni repo ekleme yönergesi

**Dürüstlük kuralı:** Komut çalıştırılmadıysa çalıştırılmış gibi yazma.
Bir test yapılmadıysa "doğrulanmadı" de. Bir araç yalnızca kurulduysa
"çalışıyor" deme. Kullanıcı onayı gerektiren adımlarda dur ve izin iste.

## 11. Ajan için ilk talimat

Bu README'yi okuduktan sonra hemen bütün kurulumları başlatma. Önce
**Aşama A --- Keşif ve rapor** bölümünü uygula. Sistem ve Antigravity
sürümünü tespit et, güncel repo belgelerini oku, yapılandırmayı
yedekleme planını hazırla ve önerilen değişiklikleri raporla. Riskli
veya sistem genelindeki değişiklikler için açık onay al. Onay ve
güvenlik incelemesinden sonra en küçük faydalı kurulumla başla; her
aşamayı test et ve sonuçlarını kaydet.
