import os
import streamlit as st
from gtts import gTTS

st.markdown(
    """
    <div align="center">
        <h1>Text2Talk</h1>
    </div>
    """,unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color: #D3D3D3 ; padding: 10px; border-radius: 20px;margin-bottom:10px" align="center">
        <h4>Supports 85 Languages!</h4>
        <p>Enter text in your preferred language, select your language and voice options, and convert it to speech.
        </p>
    </div>
    """, unsafe_allow_html=True
)
text=st.text_area("Enter Text to Convert to Speech", placeholder="Type here ...")

language = st.selectbox("Select Language",['English(en)', 'France(fr)', 'German(de)', 'Spanish(es)', 'Italian(it)', 'Portuguese(pt)', 'Russian(ru)', 'Chinese(zh)', 'Japanese(ja)', 'Korean(ko)', 'Arabic(ar)', 'Hindi(hi)', 'Turkish(tr)', 'Dutch(nl)', 'Polish(pl)', 'Swedish(sv)', 'Danish(da)', 'Norwegian(no)', 'Finnish(fi)', 'Czech(cs)', 'Hungarian(hu)', 'Romanian(ro)', 'Greek(el)', 'Indonesian(id)', 'Thai(th)', 'Telugu(te)', 'Vietnamese(vi)', 'Catalan(ca)', 'Hebrew(iw)', 'Serbian(sr)', 'Slovak(sk)', 'Ukrainian(uk)', 'Bulgarian(bg)', 'Croatian(hr)', 'Slovenian(sl)', 'Lithuanian(lt)', 'Filipino(tl)', 'Latvian(lv)', 'Estonian(et)', 'Maltese(mt)', 'Icelandic(is)', 'Gaelic(gd)', 'Welsh(cy)', 'Basque(eu)', 'Breton(br)', 'Corsican(co)', 'Alemannic(als)', 'Bavarian(bar)', 'Lombard(lmo)', 'Occitan(oc)', 'Picard(pcd)', 'Walloon(wa)', 'Aragonese(an)', 'Asturian(ast)', 'Aymara(ay)', 'Bambara(bm)', 'Bislama(bi)', 'Chichewa(ny)', 'Fijian(fj)', 'Frisian(fy)', 'Galician(gl)', 'Greenlandic(kl)', 'Haitian Creole(ht)', 'Hawaiian(haw)', 'Hmong(hm)', 'Igbo(ig)', 'Inuktitut(iu)', 'Javanese(jv)', 'Kinyarwanda(rw)', 'Kirundi(rn)', 'Kurdish(ku)', 'Lao(lo)', 'Luxembourgish(lb)', 'Malagasy(mg)', 'Malay(ms)', 'Maori(mi)', 'Marshallese(mh)', 'Mongolian(mn)', 'Nauruan(nr)', 'Navajo(nv)', 'Ndebele(nd)', 'Ndebele(nr)', 'Nyanja(ng)', 'Oromo(om)', 'Papiamento(pap)'])
tld = st.selectbox("Select accent",['Us English(us)','British English(co.uk)','Australian English(com.au)','Indian English(co.in)','Canadian English(ca)'])
voice_speed = st.radio("Choose Voice Speed",['Normal', 'Slow'])

if st.button("Convert to Speech"):
    if text.strip():
        tts = gTTS(text, lang=language.split('(')[1].split(')')[0], slow=(voice_speed=='Slow'), tld=tld.split('(')[1].split(')')[0])
        audio_file = 'output.mp3'
        tts.save(audio_file)
        st.audio(audio_file, format='audio/mp3')
        st.download_button(
            label="Download Audio",
            data=open(audio_file, 'rb'),
            file_name='output.mp3',
            mime='audio/mp3'
        )
        os.remove(audio_file)
    else:
        st.warning("Please enter text to convert to speech")
