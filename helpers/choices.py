DIVISION_CHOICES = [
    ('dhaka', 'ঢাকা'),
    ('chittagong', 'চট্টগ্রাম'),
    ('rajshahi', 'রাজশাহী'),
    ('khulna', 'খুলনা'),
    ('barisal', 'বরিশাল'),
    ('sylhet', 'সিলেট'),
    ('rangpur', 'রংপুর'),
    ('mymensingh', 'ময়মনসিংহ'),
]

DHAKA_DIVISION_DISTRICTS = [
    ('dhaka', 'ঢাকা'), ('faridpur', 'ফরিদপুর'), ('gazipur', 'গাজীপুর'),
    ('gopalganj', 'গোপালগঞ্জ'), ('jamalpur', 'জামালপুর'), ('kishoreganj', 'কিশোরগঞ্জ'),
    ('madaripur', 'মাদারীপুর'), ('manikganj', 'মানিকগঞ্জ'), ('munshiganj', 'মুন্সিগঞ্জ'),
    ('narayanganj', 'নারায়ণগঞ্জ'), ('narsingdi', 'নরসিংদী'), ('netrokona', 'নেত্রকোণা'),
    ('rajbari', 'রাজবাড়ী'), ('shariatpur', 'শরীয়তপুর'), ('sherpur', 'শেরপুর'), ('tangail', 'টাঙ্গাইল'),
]

DHAKA_UPAZILAS = {
    'dhaka': [('dhaka_sadar', 'ঢাকা সদর'), ('savar', 'সাভার'), ('dohar', 'দোহার'), ('keraniganj', 'কেরানীগঞ্জ'), ('nawabganj', 'নবাবগঞ্জ')],
    'faridpur': [('faridpur_sadar', 'ফরিদপুর সদর'), ('bhanga', 'ভাঙ্গা'), ('boalmari', 'বোয়ালমারী'), ('saltha', 'সালথা'), ('charbhadrasan', 'চরভদ্রাসন'), ('madarchar', 'মাদারচর'), ('nagaranda', 'নগরকান্দা'), ('sadarpur', 'সদরপুর'), ('alkhali', 'আলফাডাঙ্গা')],
    'gazipur': [('gazipur_sadar', 'গাজীপুর সদর'), ('tongi', 'টঙ্গী'), ('sreepur', 'শ্রীপুর'), ('kaliganj', 'কালীগঞ্জ'), ('kapasia', 'কাপাসিয়া'), ('kaliakair', 'কালিয়াকৈর')],
    'gopalganj': [('gopalganj_sadar', 'গোপালগঞ্জ সদর'), ('kashiani', 'কাশীয়ানী'), ('tungipara', 'তুংগীপারা'), ('kotalipara', 'কোটালীপাড়া'), ('muksudpur', 'মুকসুদপুর')],
    'jamalpur': [('jamalpur_sadar', 'জামালপুর সদর'), ('melandaha', 'মেলান্দহ'), ('dewanganj', 'দেওয়ানগঞ্জ'), ('bakshiganj', 'বকশীগঞ্জ'), ('islampur', 'ইসলামপুর'), ('madarganj', 'মাদারগঞ্জ'), ('sarishabari', 'সরিষাবাড়ী')],
    'kishoreganj': [('kishoreganj_sadar', 'কিশোরগঞ্জ সদর'), ('hossainpur', 'হোসেনপুর'), ('pakundia', 'পাকুন্দিয়া'), ('katiadi', 'কাটিয়াদী'), ('bhairab', 'ভৈরব'), ('tarail', 'টারাইল'), ('bajitpur', 'বাজিতপুর'), ('mithamain', 'মিঠামইন'), ('nikli', 'নিকলী'), ('kuliarchar', 'কুলিয়ারচর'), ('itna', 'ইটনা'), ('ashtagram', 'অষ্টগ্রাম')],
    'madaripur': [('madaripur_sadar', 'মাদারীপুর সদর'), ('rajoir', 'রাজৈর'), ('kalkini', 'কালকিনি'), ('sibchar', 'শিবচর'), ('dasar', 'ডাসার')],
    'manikganj': [('manikganj_sadar', 'মানিকগঞ্জ সদর'), ('saturia', 'সাটুরিয়া'), ('harirampur', 'হরিরামপুর'), ('ghior', 'ঘিওর'), ('daulatpur', 'দৌলতপুর'), ('singair', 'সিংগাইর'), ('shibalaya', 'শিবালয়')],
    'munshiganj': [('munshiganj_sadar', 'মুন্সিগঞ্জ সদর'), ('sreenagar', 'শ্রীনগর'), ('serajdikhan', 'সিরাজদিখান'), ('lauhajang', 'লৌহজং'), ('gazaria', 'গজারিয়া'), ('tongibari', 'টংগিবাড়ী')],
    'narayanganj': [('narayanganj_sadar', 'নারায়ণগঞ্জ সদর'), ('siddirganj', 'সিদ্ধিরগঞ্জ'), ('araihazar', 'আড়াইহাজার'), ('bandar', 'বন্দর'), ('sonargaon', 'সোনারগাঁও'), ('rupganj', 'রূপগঞ্জ')],
    'narsingdi': [('narsingdi_sadar', 'নরসিংদী সদর'), ('belabo', 'বেলাবো'), ('monohardi', 'মনোহরদী'), ('shibpur', 'শিবপুর'), ('palash', 'পলাশ'), ('raipura', 'রায়পুরা')],
    'netrokona': [('netrokona_sadar', 'নেত্রকোণা সদর'), ('dhobaura', 'ধোবাউড়া'), ('kalmakanda', 'কলমাকান্দা'), ('purbadhala', 'পূর্বধলা'), ('durgapur', 'দুর্গাপুর'), ('kendua', 'কেন্দুয়া'), ('madan', 'মদন'), ('mohanganj', 'মোহনগঞ্জ'), ('atpara', 'আটপাড়া'), ('barhatta', 'বরহাট্টা')],
    'rajbari': [('rajbari_sadar', 'রাজবাড়ী সদর'), ('baliakandi', 'বালিয়াকান্দি'), ('kalukhali', 'কালুখালী'), ('pangsha', 'পাংশা'), ('goalanda', 'গোয়ালন্দ'), ('doulatdia', 'দৌলতদিয়া')],
    'shariatpur': [('shariatpur_sadar', 'শরীয়তপুর সদর'), ('naria', 'নড়িয়া'), ('jajira', 'জাজিরা'), ('bhedarganj', 'ভেদরগঞ্জ'), ('damudhya', 'ডামুড্যা'), ('gosairhat', 'গোসাইরহাট')],
    'sherpur': [('sherpur_sadar', 'শেরপুর সদর'), ('nokla', 'নকলা'), ('sribordi', 'শ্রীবরদী'), ('jhenigati', 'ঝিনাইগাতী')],
    'tangail': [('tangail_sadar', 'টাঙ্গাইল সদর'), ('sakhipur', 'সখিপুর'), ('basail', 'বাসাইল'), ('dhanbari', 'ধানবাড়ী'), ('gopalpur', 'গোপালপুর'), ('madhupur', 'মধুপুর'), ('mirzapur', 'মির্জাপুর'), ('nagarpur', 'নাগরপুর'), ('bhuyapur', 'ভুয়াপুর'), ('kalihati', 'কালিহাতী'), ('delduar', 'দেলদুয়ার')],
}

CHITTAGONG_DIVISION_DISTRICTS = [
    ('bandarban', 'বান্দরবন'), ('brahmanbaria', 'ব্রাহ্মণবাড়ীয়া'), ('chandpur', 'চাঁদপুর'),
    ('chittagong', 'চট্টগ্রাম'), ('comilla', 'কুমিল্লা'), ('cox_bazar', 'কক্সবাজার'),
    ('feni', 'ফেনী'), ('khagrachari', 'খাগড়াছড়ি'), ('lakshmipur', 'লক্ষ্মীপুর'),
    ('noakhali', 'নোয়াখালী'), ('rangamati', 'রাঙ্গামাটি'),
]

CHITTAGONG_UPAZILAS = {
    'chittagong': [('chittagong_sadar', 'চট্টগ্রাম সদর'), ('pahartali', 'পাহাড়তলী'), ('banskali', 'বাঁশখালী'), ('sitakunda', 'সীতাকুণ্ড'), ('rangunia', 'রাঙ্গুনিয়া'), ('hathazari', 'হাটহাজারী'), ('patiya', 'পটিয়া'), ('mirsharai', 'মীরসরাই'), ('anwara', 'আনোয়ারা'), ('sandwip', 'সন্দ্বীপ'), ('boalkhali', 'বোয়ালখালী'), ('fatickchhari', 'ফটিকছড়ি'), ('lohagara', 'লোহাগাড়া'), ('satkania', 'সাতকানিয়া'), ('chandanish', 'চন্দনাইশ')],
    'comilla': [('comilla_sadar', 'কুমিল্লা সদর'), ('chandina', 'চন্দিনা'), ('daudkandi', 'দাউদকান্দি'), ('laksam', 'লাকসাম'), ('nangalkot', 'নাঙ্গলকোট'), ('chaddagram', 'চৌদ্দগ্রাম'), ('burichang', 'বুড়িচং'), ('barura', 'বরুড়া'), ('debidwar', 'দেবীদ্বার'), ('homna', 'হোমনা'), ('mudhafargonj', 'মুরাদনগর'), ('meghna', 'মেঘনা'), ('titas', 'তিতাস'), ('monohargonj', 'মনোহরগঞ্জ')],
    'cox_bazar': [('cox_bazar_sadar', 'কক্সবাজার সদর'), ('ramu', 'রামু'), ('moheshkhali', 'মহেশখালী'), ('chakaria', 'চকরিয়া'), ('ukhiya', 'উখিয়া'), ('teknaf', 'টেকনাফ'), ('kutubdia', 'কুতুবদিয়া'), ('pekarua', 'পেকুয়া')],
    'noakhali': [('noakhali_sadar', 'নোয়াখালী সদর'), ('companiganj', 'কোম্পানীগঞ্জ'), ('begumganj', 'বেগমগঞ্জ'), ('hatiya', 'হাতিয়া'), ('subarnachar', 'সুবর্ণচর'), ('senbagh', 'সেনবাগ'), ('sonaimuri', 'সোনাইমুড়ী'), ('kabirhat', 'কবিরহাট')],
    'feni': [('feni_sadar', 'ফেনী সদর'), ('parshuram', 'পরশুরাম'), ('daganbhuiyan', 'দাগনভূঁইয়া'), ('sonagazi', 'সোনাগাজী'), ('fulgazi', 'ফুলগাজী'), ('chhagalnaiya', 'ছাগলনাইয়া')],
    'brahmanbaria': [('brahmanbaria_sadar', 'ব্রাহ্মণবাড়ীয়া সদর'), ('ashuganj', 'আশুগঞ্জ'), ('nabinagar', 'নবীনগর'), ('sarail', 'সরাইল'), ('bancharampur', 'বাঞ্ছারামপুর'), ('bijoynagar', 'বিজয়নগর'), ('akkhaura', 'আখাউড়া'), ('kasba', 'কসবা'), ('nasirnagar', 'নাসিরনগর')],
    'chandpur': [('chandpur_sadar', 'চাঁদপুর সদর'), ('hajiganj', 'হাজীগঞ্জ'), ('shahrasti', 'শাহরাস্তি'), ('kacharipara', 'কচুয়া'), ('matlab_dakshin', 'মতলব দক্ষিণ'), ('matlab_uttar', 'মতলব উত্তর'), ('faridganj', 'ফরিদগঞ্জ')],
    'bandarban': [('bandarban_sadar', 'বান্দরবন সদর'), ('naikhongchhari', 'নাইক্ষ্যংছড়ি'), ('rowangchhari', 'রোয়াংছড়ি'), ('ruma', 'রুমা'), ('lama', 'লামা'), ('thanchi', 'থানচি'), ('alikadam', 'আলীকদম')],
    'khagrachari': [('khagrachari_sadar', 'খাগড়াছড়ি সদর'), ('dighinala', 'দিঘিনালা'), ('panchhari', 'পানছড়ি'), ('manikchhari', 'মানিকছড়ি'), ('matiranga', 'মাটিরাঙ্গা'), ('ramgarh', 'রামগড়'), ('lakshmichhari', 'লক্ষ্মীছড়ি'), ('mohalchari', 'মহালছড়ি')],
    'lakshmipur': [('lakshmipur_sadar', 'লক্ষ্মীপুর সদর'), ('ramganj', 'রামগঞ্জ'), ('ramgati', 'রামগতি'), ('raipur', 'রায়পুর'), ('kamalnagar', 'কমলনগর')],
    'rangamati': [('rangamati_sadar', 'রাঙ্গামাটি সদর'), ('kaptai', 'কাপ্তাই'), ('kawkhali', 'কাউখালী'), ('baghaichhari', 'বাঘাইছড়ি'), ('barkal', 'বারকাল'), ('langadu', 'লঙ্গাদু'), ('belaichhari', 'বেলাইছড়ি'), ('juraichhari', 'জুরাইছড়ি'), ('naniachar', 'নানিয়ারচর')],
}

RAJSHAHI_DIVISION_DISTRICTS = [
    ('bogra', 'বগুড়া'), ('chapainawabganj', 'চাঁপাইনবাবগঞ্জ'), ('jaipurhat', 'জয়পুরহাট'),
    ('naogaon', 'নওগাঁ'), ('natore', 'নাটোর'), ('pabna', 'পাবনা'),
    ('rajshahi', 'রাজশাহী'), ('sirajganj', 'সিরাজগঞ্জ'),
]

RAJSHAHI_UPAZILAS = {
    'rajshahi': [('rajshahi_sadar', 'রাজশাহী সদর'), ('paba', 'পবা'), ('durgapur', 'দুর্গাপুর'), ('bagmara', 'বাগমারা'), ('mohanpur', 'মোহনপুর'), ('tanore', 'তানোর'), ('godagari', 'গোদাগাড়ী'), ('boalia', 'বোয়ালিয়া'), ('charget', 'চারঘাট'), ('puthia', 'পুঠিয়া'), ('bagha', 'বাঘা')],
    'bogra': [('bogra_sadar', 'বগুড়া সদর'), ('sariakandi', 'সারিয়াকান্দি'), ('shajahanpur', 'শাজাহানপুর'), ('gabtali', 'গাবতলী'), ('sonatala', 'সোনাতলা'), ('dhunat', 'ধুনট'), ('nandigram', 'নন্দীগ্রাম'), ('shibganj', 'শিবগঞ্জ'), ('adamdighi', 'আদমদীঘি'), ('dupunchaniya', 'দুপচাঁচিয়া'), ('kahaloo', 'কাহালু')],
    'pabna': [('pabna_sadar', 'পাবনা সদর'), ('ishwardi', 'ঈশ্বরদী'), ('sujanagar', 'সুজানগর'), ('santhiya', 'সাঁথিয়া'), ('bera', 'বেড়া'), ('bhangura', 'ভাঙ্গুড়া'), ('atgharia', 'আটঘরিয়া'), ('faridpur_pabna', 'ফরিদপুর'), ('chatmohar', 'চাটমোহর')],
    'naogaon': [('naogaon_sadar', 'নওগাঁ সদর'), ('manda', 'মান্দা'), ('niamatpur', 'নিয়ামতপুর'), ('badalgachi', 'বদলগাছী'), ('patnitala', 'পত্নীতলা'), ('dhamoirhat', 'ধামইরহাট'), ('sapahar', 'সাপাহার'), ('porsha', 'পোরশা'), ('raninagar', 'রাণীনগর'), ('mahadevpur', 'মহাদেবপুর'), ('atrakhi', 'আত্রাই')],
    'natore': [('natore_sadar', 'নাটোর সদর'), ('bagatipara', 'বাগাতিপাড়া'), ('baraigram', 'বড়াইগ্রাম'), ('gurudaspur', 'গুরুদাসপুর'), ('lalpur', 'লালপুর'), ('singra', 'সিংড়া'), ('naldu', 'নলডাঙ্গা')],
    'sirajganj': [('sirajganj_sadar', 'সিরাজগঞ্জ সদর'), ('shahjadpur', 'শাহজাদপুর'), ('ullapara', 'উল্লাপাড়া'), ('belkuchi', 'বেলকুচি'), ('kamarkhanda', 'কামারখন্দ'), ('tarash', 'তারাশ'), ('raiganj', 'রায়গঞ্জ'), ('chauhali', 'চৌহালি'), ('kaziipur', 'কাজীপুর')],
    'chapainawabganj': [('chapainawabganj_sadar', 'চাঁপাইনবাবগঞ্জ সদর'), ('gomastapur', 'গোমস্তাপুর'), ('nawabganj_cha', 'নবাবগঞ্জ'), ('shibganj_cha', 'শিবগঞ্জ'), ('bholahat', 'ভোলাহাট')],
    'jaipurhat': [('jaipurhat_sadar', 'জয়পুরহাট সদর'), ('akkela', 'আক্কেলপুর'), ('kalai', 'কালাই'), ('khetlal', 'ক্ষেতলাল'), ('panchbibi', 'পাঁচবিবি')],
}

KHULNA_DIVISION_DISTRICTS = [
    ('bagerhat', 'বাগেরহাট'), ('chuadanga', 'চুয়াডাঙ্গা'), ('jessore', 'যশোর'),
    ('jhenaidah', 'ঝিনাইদহ'), ('khulna', 'খুলনা'), ('kustia', 'কুষ্টিয়া'),
    ('magura', 'মাগুরা'), ('meherpur', 'মেহেরপুর'), ('narail', 'নড়াইল'), ('satkhira', 'সাতক্ষীরা'),
]

KHULNA_UPAZILAS = {
    'khulna': [('khulna_sadar', 'খুলনা সদর'), ('dighalia', 'দিঘলিয়া'), ('phultala', 'ফুলতলা'), ('rupsha', 'রূপসা'), ('terokhada', 'তেরোখাদা'), ('dacope', 'ডাকোপ'), ('paikgacha', 'পাইকগাছা'), ('koyra', 'কয়রা'), ('batiaghata', 'বটিয়াঘাটা'), ('dumuria', 'ডুমুরিয়া')],
    'jessore': [('jessore_sadar', 'যশোর সদর'), ('bagherpara', 'বাঘেরপাড়া'), ('chowgacha', 'চৌগাছা'), ('jhikargacha', 'ঝিকরগাছা'), ('keshabpur', 'কেশবপুর'), ('manirampur', 'মণিরামপুর'), ('sarsha', 'সরশা'), ('abahaynanagar', 'অভয়নগর'), ('shyamnagar', 'শ্যামনগর'), ('kaliganj_jes', 'কালীগঞ্জ')],
    'satkhira': [('satkhira_sadar', 'সাতক্ষীরা সদর'), ('kalaroa', 'কালারোয়া'), ('tala', 'তালা'), ('assassuni', 'আশাশুনি'), ('debhata', 'দেবহাটা'), ('patkelghata', 'পাটকেলঘাটা'), ('shyamnagar_sat', 'শ্যামনগর')],
    'bagerhat': [('bagerhat_sadar', 'বাগেরহাট সদর'), ('fakirhat', 'ফকিরহাট'), ('mollahat', 'মোল্লাহাট'), ('chitalmari', 'চিতলমারী'), ('rampal', 'রামপাল'), ('khuakhali', 'কচুয়া'), ('morrelganj', 'মোড়েলগঞ্জ'), ('sarankhola', 'শরণখোলা'), ('mathbaria', 'মঠবাড়িয়া')],
    'chuadanga': [('chuadanga_sadar', 'চুয়াডাঙ্গা সদর'), ('alamdanga', 'আলমডাঙ্গা'), ('damurhuda', 'দামুড়হুদা'), ('jibannagar', 'জীবননগর')],
    'jhenaidah': [('jhenaidah_sadar', 'ঝিনাইদহ সদর'), ('maheshpur', 'মহেশপুর'), ('kaliganj_jhe', 'কালীগঞ্জ'), ('kotchandpur', 'কোটচাঁদপুর'), ('shailkupa', 'শৈলকুপা'), ('harinakunda', 'হরিণাকুন্ডু')],
    'kustia': [('kustia_sadar', 'কুষ্টিয়া সদর'), ('kumarkhali', 'কুমারখালী'), ('khoksa', 'খোকসা'), ('mirpur', 'মিরপুর'), ('daulatpur_kus', 'দৌলতপুর'), ('vheramara', 'ভেড়ামারা')],
    'magura': [('magura_sadar', 'মাগুরা সদর'), ('shalikha', 'শালিখা'), ('sreepur_mag', 'শ্রীপুর'), ('mohammadpur_mag', 'মহম্মদপুর')],
    'meherpur': [('meherpur_sadar', 'মেহেরপুর সদর'), ('mujibnagar', 'মুজিবনগর'), ('gangni', 'গাংনী')],
    'narail': [('narail_sadar', 'নড়াইল সদর'), ('lohagara_nar', 'লোহাগড়া'), ('kalia_nar', 'কালিয়া')],
}

BARISAL_DIVISION_DISTRICTS = [
    ('barguna', 'বরগুনা'), ('barisal', 'বরিশাল'), ('bhola', 'ভোলা'),
    ('jhalokati', 'ঝালকাঠী'), ('patuakhali', 'পটুয়াখালী'), ('pirojpur', 'পিরোজপুর'),
]

BARISAL_UPAZILAS = {
    'barisal': [('barisal_sadar', 'বরিশাল সদর'), ('bakerganj', 'বাকেরগঞ্জ'), ('gournadi', 'গৌরনদী'), ('babuganj', 'বাবুগঞ্জ'), ('wazirpur', 'ওয়াজিরপুর'), ('muladi', 'মুলাদী'), ('hizla', 'হিজলা'), ('barisal_mehendiganj', 'মেহেন্দিগঞ্জ'), ('banaripara', 'বানারীপাড়া'), ('agaijhara', 'আগৈলঝারা')],
    'bhola': [('bhola_sadar', 'ভোলা সদর'), ('char_fassion', 'চরফ্যাশন'), ('monpura', 'মনপুরা'), ('lalmohan', 'লালমোহন'), ('tazumuddin', 'তজুমুদ্দিন'), ('borhanuddin', 'বোরহানউদ্দিন'), ('daulatkhan', 'দৌলতখান')],
    'barguna': [('barguna_sadar', 'বরগুনা সদর'), ('amtali', 'আমতলী'), ('bamna', 'বামনা'), ('betagi', 'বেতাগী'), ('patharghata', 'পাথরঘাটা')],
    'jhalokati': [('jhalokati_sadar', 'ঝালকাঠী সদর'), ('natchole', 'নাচোল'), ('kathalia', 'কাঠালিয়া'), ('rajapur_jha', 'রাজাপুর')],
    'patuakhali': [('patuakhali_sadar', 'পটুয়াখালী সদর'), ('bauphal', 'বাউফল'), ('dashmina', 'দশমিনা'), ('galachipa', 'গলাচিপা'), ('kalapara', 'কলাপাড়া'), ('mirzaganj', 'মির্জাগঞ্জ'), ('dumki', 'ডুমকি'), ('rangabali', 'রাঙ্গাবালী')],
    'pirojpur': [('pirojpur_sadar', 'পিরোজপুর সদর'), ('mothbaria', 'মঠবাড়িয়া'), ('nazirpur', 'নাজিরপুর'), ('bhandaria', 'ভাণ্ডারিয়া'), ('zianagar', 'জিয়ানগর'), ('nazirpur_pir', 'নেছারাবাদ'), ('kawkhali_pir', 'কাউখালী')],
}

SYLHET_DIVISION_DISTRICTS = [
    ('habiganj', 'হবিগঞ্জ'), ('moulvibazar', 'মৌলভীবাজার'), ('sunamganj', 'সুনামগঞ্জ'), ('sylhet', 'সিলেট'),
]

SYLHET_UPAZILAS = {
    'sylhet': [('sylhet_sadar', 'সিলেট সদর'), ('balaganj', 'বালাগঞ্জ'), ('beanibazar', 'বিয়ানীবাজার'), ('golapganj', 'গোলাপগঞ্জ'), ('jaintiapur', 'জৈন্তাপুর'), ('kanajghat', 'কানাইঘাট'), ('southern_surma', 'দক্ষিণ সুরমা'), ('fenchuganj', 'ফেঞ্চুগঞ্জ'), ('bishwanath', 'বিশ্বনাথ'), ('zakiganj', 'জকিগঞ্জ'), ('companyganj_syl', 'কোম্পানীগঞ্জ'), ('gowainghat', 'গোয়াইনঘাট')],
    'moulvibazar': [('moulvibazar_sadar', 'মৌলভীবাজার সদর'), ('sreemangal', 'শ্রীমঙ্গল'), ('kamalganj', 'কমলগঞ্জ'), ('rajnagar', 'রাজনগর'), ('kulaora', 'কুলাউড়া'), ('baralekha', 'বড়লেখা'), ('juri', 'জুড়ী')],
    'habiganj': [('habiganj_sadar', 'হবিগঞ্জ সদর'), ('nabiganj', 'নবীগঞ্জ'), ('bahubal', 'বাহুবল'), ('ajmiriganj', 'আজমিরীগঞ্জ'), ('baniachang', 'বানিয়াচং'), ('lakhai', 'লাখাই'), ('chunarughat', 'চুনারুঘাট'), ('madhabpur', 'মাধবপুর')],
    'sunamganj': [('sunamganj_sadar', 'সুনামগঞ্জ সদর'), ('dharamapasha', 'ধর্মপাশা'), ('jamalganj', 'জামালগঞ্জ'), ('sullah', 'শাল্লা'), ('derai', 'দিরাই'), ('chhatak', 'ছাতক'), ('dowarabazar', 'দোয়ারাবাজার'), ('tahirpur', 'তাহিরপুর'), ('bishambharpur', 'বিশম্ভরপুর')],
}

RANGPUR_DIVISION_DISTRICTS = [
    ('dinajpur', 'দিনাজপুর'), ('gaibandha', 'গাইবান্ধা'), ('kurigram', 'কুড়িগ্রাম'),
    ('lalmonirhat', 'লালমনিরহাট'), ('nilphamari', 'নীলফামারী'), ('panchagarh', 'পঞ্চগড়'),
    ('rangpur', 'রংপুর'), ('thakurgaon', 'ঠাকুরগাঁও'),
]

RANGPUR_UPAZILAS = {
    'rangpur': [('rangpur_sadar', 'রংপুর সদর'), ('badarganj', 'বদরগঞ্জ'), ('gangachara', 'গঙ্গাচরা'), ('taraganj', 'তারাগঞ্জ'), ('kaunia', 'কাউনিয়া'), ('porsha_rang', 'পোরশা'), ('mithapukur', 'মিঠাপুকুর'), ('pirgacha', 'পীরগাছা'), ('pirsadar', 'পীরগঞ্জ')],
    'dinajpur': [('dinajpur_sadar', 'দিনাজপুর সদর'), ('birganj', 'বীরগঞ্জ'), ('parbatipur', 'পার্বতীপুর'), ('biral', 'বিরল'), ('bochaganj', 'বোচাগঞ্জ'), ('kaharole', 'কাহারোল'), ('phulbari', 'ফুলবাড়ী'), ('nawabganj_din', 'নবাবগঞ্জ'), ('ghoraghat', 'ঘোড়াঘাট'), ('hili', 'হিলি'), ('birampur', 'বিরামপুর'), ('hoksa_din', 'খানসামা'), ('chirirbandar', 'চিরিরবন্দর')],
    'gaibandha': [('gaibandha_sadar', 'গাইবান্ধা সদর'), ('sadullahpur', 'সাদুল্লাপুর'), ('saghata', 'সাঘাটা'), ('gobindaganj', 'গোবিন্দগঞ্জ'), ('sunatganj', 'সুন্দরগঞ্জ'), ('pulbari_gai', 'পলাশবাড়ী')],
    'kurigram': [('kurigram_sadar', 'কুড়িগ্রাম সদর'), ('nageshwari', 'নাগেশ্বরী'), ('bhurungamari', 'ভুরুঙ্গামারী'), ('phulbari_kur', 'ফুলবাড়ী'), ('rajarhat', 'রাজারহাট'), ('ulipur', 'উলিপুর'), ('chilmari', 'চিলমারী'), ('rowmari', 'রৌমারী'), ('maynaguri', 'ময়নাগুড়ি')],
    'lalmonirhat': [('lalmonirhat_sadar', 'লালমনিরহাট সদর'), ('patgram', 'পাটগ্রাম'), ('hatibandha', 'হাতীবান্ধা'), ('kaliganj_lal', 'কালীগঞ্জ'), ('aditmari', 'আদিতমারী')],
    'nilphamari': [('nilphamari_sadar', 'নীলফামারী সদর'), ('saidpur', 'সৈয়দপুর'), ('dimla', 'ডিমলা'), ('domar', 'ডোমার'), ('kishoreganj_nil', 'কিশোরগঞ্জ'), ('jaldhaka', 'জলঢাকা')],
    'panchagarh': [('panchagarh_sadar', 'পঞ্চগড় সদর'), ('debiganj', 'দেবীগঞ্জ'), ('tetulia', 'তেতুলিয়া'), ('bochaganj_pan', 'বোদা'), ('atwari', 'আটোয়ারী')],
    'thakurgaon': [('thakurgaon_sadar', 'ঠাকুরগাঁও সদর'), ('baliadangi', 'বালিয়াডাঙ্গি'), ('haripur', 'হরিপুর'), ('ranisankail', 'রাণীশংকৈল'), ('pirganj', 'পীরগঞ্জ')],
}

MYMENSINGH_DIVISION_DISTRICTS = [
    ('jamalpur', 'জামালপুর'), ('mymensingh', 'ময়মনসিংহ'), ('netrokona', 'নেত্রকোণা'), ('sherpur', 'শেরপুর'),
]

MYMENSINGH_UPAZILAS = {
    'mymensingh': [('mymensingh_sadar', 'ময়মনসিংহ সদর'), ('fulpur', 'ফুলপুর'), ('muktagacha', 'মুক্তাগাছা'), ('trishal', 'ত্রিশাল'), ('gouripur', 'গৌরীপুর'), ('ishwarganj', 'ঈশ্বরগঞ্জ'), ('halueaghat', 'হালুয়াঘাট'), ('nandail', 'নান্দাইল'), ('phulbaria_mym', 'ফুলবাড়িয়া'), ('bhaluka', 'ভালুকা'), ('tarakanda', 'তারাকান্দা'), ('dhobaura_mym', 'ধোবাউড়া')],
}

DISTRICT_CHOICES = (
    DHAKA_DIVISION_DISTRICTS +
    CHITTAGONG_DIVISION_DISTRICTS +
    RAJSHAHI_DIVISION_DISTRICTS +
    KHULNA_DIVISION_DISTRICTS +
    BARISAL_DIVISION_DISTRICTS +
    SYLHET_DIVISION_DISTRICTS +
    RANGPUR_DIVISION_DISTRICTS +
    MYMENSINGH_DIVISION_DISTRICTS
)

UPAZILA_CHOICES = []
for upazila_dict in [DHAKA_UPAZILAS, CHITTAGONG_UPAZILAS, RAJSHAHI_UPAZILAS, KHULNA_UPAZILAS, BARISAL_UPAZILAS, SYLHET_UPAZILAS, RANGPUR_UPAZILAS, MYMENSINGH_UPAZILAS]:
    for district_upazilas in upazila_dict.values():
        UPAZILA_CHOICES.extend(district_upazilas)

PLACE_TYPE_CHOICES = [
    ('village', 'গ্রাম'), ('city', 'শহর'), ('area', 'এলাকা'),
    ('mohalla', 'মহল্লা'), ('para', 'পাড়া'), ('ward', 'ওয়ার্ড'), ('union', 'ইউনিয়ন'),
]

SERVICE_TYPE_CHOICES = [
    ('cooking', 'রান্না করা'),
    ('cleaning', 'ঘর পরিষ্কার'),
    ('childcare', 'শিশু পরিচর্যা'),
    ('elderly_care', 'বৃদ্ধ সেবা'),
    ('gardening', 'বাগান করা'),
    ('car_washing', 'গাড়ি ধোয়া'),
    ('laundry', 'কাপড় ধোয়া'),
    ('shopping', 'বাজার করা'),
    ('babysitting', 'বেবিসিটিং'),
    ('caregiver', 'কেয়ারগিভার'),
    ('plumber', 'প্লাম্বার'),
    ('electrician', 'ইলেকট্রিশিয়ান'),
    ('carpenter', 'ছুতার'),
    ('painter', 'পেন্টার'),
    ('welder', 'ওয়েল্ডার'),
    ('mason', 'রাজমিস্ত্রি'),
    ('driver', 'ড্রাইভার'),
    ('security_guard', 'সিকিউরিটি গার্ড'),
    ('office_assistant', 'অফিস সহায়ক'),
    ('delivery_man', 'ডেলিভারি ম্যান'),
    ('tailor', 'দর্জি'),
    ('beautician', 'বিউটিশিয়ান'),
    ('masseur', 'ম্যাসিউর'),
    ('nurse', 'নার্স'),
    ('physiotherapist', 'ফিজিওথেরাপিস্ট'),
    ('tutor', 'টিউটর'),
    ('event_worker', 'ইভেন্ট ওয়ার্কার'),
    ('pest_control', 'পেস্ট কন্ট্রোল'),
    ('moving_help', 'মুভিং হেল্প'),
    ('pet_care', 'পোষ্য পরিচর্যা'),
    ('home_repair', 'বাড়ি মেরামত'),
    ('ac_technician', 'এসি টেকনিশিয়ান'),
    ('generator_tech', 'জেনারেটর টেকনিশিয়ান'),
    ('computer_repair', 'কম্পিউটার মেরামত'),
    ('mobile_repair', 'মোবাইল মেরামত'),
]

AVAILABILITY_CHOICES = [
    ('available', 'উপলব্ধ'), ('busy', 'ব্যস্ত'), ('unavailable', 'অনুপলব্ধ'),
]

HIRING_STATUS_CHOICES = [
    ('pending', 'অপেক্ষমাণ'), ('active', 'সক্রিয়'),
    ('completed', 'সম্পন্ন'), ('cancelled', 'বাতিল'),
]

ACCOUNT_TYPE_CHOICES = [
    ('user', 'সাধারণ ব্যবহারকারী'), ('helper', 'হেল্পার'),
]

SERVICE_TYPE_ICONS = {
    'cooking': '🍳', 'cleaning': '🧹', 'childcare': '👶', 'elderly_care': '👴',
    'gardening': '🌱', 'car_washing': '🚗', 'laundry': '👕', 'shopping': '🛒',
    'babysitting': '🍼', 'caregiver': '🤝', 'plumber': '🔧', 'electrician': '⚡',
    'carpenter': '🪚', 'painter': '🎨', 'welder': '🔥', 'mason': '🧱',
    'driver': '🚙', 'security_guard': '🛡️', 'office_assistant': '📋', 'delivery_man': '📦',
    'tailor': '✂️', 'beautician': '💄', 'masseur': '💆', 'nurse': '🏥',
    'physiotherapist': '🦴', 'tutor': '📚', 'event_worker': '🎪', 'pest_control': '🐜',
    'moving_help': '📦', 'pet_care': '🐾', 'home_repair': '🔨', 'ac_technician': '❄️',
    'generator_tech': '⚙️', 'computer_repair': '💻', 'mobile_repair': '📱',
}

SERVICE_CATEGORIES = [
    ('domestic', 'গৃহস্থালি সেবা', ['cooking', 'cleaning', 'laundry', 'shopping', 'gardening', 'car_washing']),
    ('care', 'যত্ন সেবা', ['childcare', 'elderly_care', 'babysitting', 'caregiver', 'pet_care']),
    ('repair', 'মেরামত সেবা', ['plumber', 'electrician', 'carpenter', 'painter', 'welder', 'mason', 'home_repair', 'ac_technician', 'generator_tech', 'computer_repair', 'mobile_repair']),
    ('professional', 'পেশাদার সেবা', ['driver', 'security_guard', 'office_assistant', 'delivery_man', 'tailor', 'beautician', 'masseur', 'nurse', 'physiotherapist', 'tutor', 'event_worker', 'pest_control', 'moving_help']),
]


def get_districts_by_division(division_code):
    district_map = {
        'dhaka': DHAKA_DIVISION_DISTRICTS,
        'chittagong': CHITTAGONG_DIVISION_DISTRICTS,
        'rajshahi': RAJSHAHI_DIVISION_DISTRICTS,
        'khulna': KHULNA_DIVISION_DISTRICTS,
        'barisal': BARISAL_DIVISION_DISTRICTS,
        'sylhet': SYLHET_DIVISION_DISTRICTS,
        'rangpur': RANGPUR_DIVISION_DISTRICTS,
        'mymensingh': MYMENSINGH_DIVISION_DISTRICTS,
    }
    return district_map.get(division_code, [])


def get_upazilas_by_district(district_code):
    all_upazilas = {**DHAKA_UPAZILAS, **CHITTAGONG_UPAZILAS, **RAJSHAHI_UPAZILAS, **KHULNA_UPAZILAS, **BARISAL_UPAZILAS, **SYLHET_UPAZILAS, **RANGPUR_UPAZILAS, **MYMENSINGH_UPAZILAS}
    return all_upazilas.get(district_code, [])
