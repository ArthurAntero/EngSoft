import sys
import os
import streamlit as st
from _pages.Login import create_login_page

# Adiciona o diretório "src" ao Python Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Teste apenas da página de Login
create_login_page()
