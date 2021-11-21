import streamlit as st
from PIL import Image
import pathlib
import os
import datetime

ss=pathlib.Path(r"C:\Users\na489\Documents\My Games\FINAL FANTASY XIV - A Realm Reborn\screenshots\\").glob("*.png")
sslist=list(ss)



st.title("さすらい猫SS置き場(初期化３回目)")
"SSとったら自動で勝手にうｐされるやつ"

for i in sslist:
    img=Image.open(i)  
    date=datetime.datetime.fromtimestamp(os.path.getctime(i))
    st.image(img,caption=date.date())


