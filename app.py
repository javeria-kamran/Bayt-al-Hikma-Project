import streamlit as st
from database import add_book, get_all_books, delete_book
import pandas as pd
from datetime import date
import plotly.express as px

def export_books():
    books = get_all_books()
    data = [{"Title": book.title, "Author": book.author, "Genre": book.genre, "Added On": book.added_on} for book in books]
    df = pd.DataFrame(data)
    return df.to_csv(index=False).encode('utf-8')

st.set_page_config(page_title="𓋹𓂀 Bayt-al-Hikma 𓂀𓋹", layout="wide", page_icon="📜")

# Custom CSS for UI
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    * {{ 
        font-family: 'Space Grotesk', sans-serif !important;
        transition: all 0.3s ease;
    }}
    
    .main {{
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff !important;
    }}
    
    .stButton>button {{
        background: linear-gradient(45deg, #7F00FF, #E100FF);
        border: none !important;
        border-radius: 15px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 20px rgba(127, 0, 255, 0.3);
    }}
    
    .stTextInput>div>div>input {{
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid #7F00FF !important;
        border-radius: 10px !important;
    }}
    
    .sidebar .sidebar-content {{
        background: linear-gradient(195deg, #0f0c29 30%, #302b63 100%) !important;
        border-right: 2px solid #7F00FF !important;
    }}
    
    .book-card {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #7F00FF !important;
        backdrop-filter: blur(10px);
    }}
    
    .metric-card {{
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #7F00FF;
    }}
    
    .hover-glow:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(127, 0, 255, 0.4) !important;
    }}
    
    </style>
""", unsafe_allow_html=True)

# Animated Header
st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(45deg, #7F00FF, #E100FF);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        <h1 style="font-size: 3.5rem; margin: 0; font-weight: 700;">𓋹𓂀 Bayt-al-Hikma 𓂀𓋹</h1>
        <p style="font-size: 1.2rem; letter-spacing: 2px;">Digital Archive of Infinite Wisdom</p>
    </div>
""", unsafe_allow_html=True)

# Holographic Sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="font-size: 2rem; background: linear-gradient(45deg, #7F00FF, #E100FF);
                     -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                📖 Celestial Archive
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Genre Filter
    books = get_all_books()
    filter_genre = st.selectbox("🔮 Filter by Cosmic Genre", 
                               ["All"] + sorted(list(set(book.genre for book in books))),
                               key="genre_filter")

# Main Content
col1, col2 = st.columns([1, 2])

with col1:
    # Add Book Form in Glassmorphic Card
    with st.form("add_book_form", clear_on_submit=True):
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.05); padding: 2rem; border-radius: 15px;
                     border: 1px solid rgba(127, 0, 255, 0.3); backdrop-filter: blur(10px);">
                <h3 style="color: #7F00FF; margin-bottom: 1.5rem;">𓆣 Add New Tome</h3>
        """, unsafe_allow_html=True)
        
        title = st.text_input("📜 Scroll Title")
        author = st.text_input("🖋️ Scribe's Name")
        genre = st.selectbox("🌌 Cosmic Category", 
                            ["Fiction", "Non-fiction", "Mystery", "Fantasy", 
                             "Sci-Fi", "Biography", "History", "Other"])
        
        if st.form_submit_button("𓃑 Enshrine in Archive"):
            if title and author:
                add_book(title, author, genre)
                st.success(f"🌀 '{title}' has joined the cosmic collection!")
                st.balloons()

#Book Display
with col2:
    st.markdown("### 𓅰 Celestial Collection")
    
    filtered_books = [book for book in books if filter_genre in ["All", book.genre]]
    
    if filtered_books:
        for book in filtered_books:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"""
                        <div class="book-card hover-glow">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div style="flex-grow: 1;">
                                    <h4 style="margin: 0; color: #E100FF;">{book.title}</h4>
                                    <p style="margin: 5px 0; font-size: 0.9em; color: #aaa;">𓍯 {book.author}</p>
                                    <div style="display: flex; gap: 10px; align-items: center;">
                                        <span style="background: rgba(127, 0, 255, 0.2); padding: 3px 10px;
                                                    border-radius: 15px; font-size: 0.8em;">
                                            {book.genre}
                                        </span>
                                        <span style="font-size: 0.8em; color: #888;">
                                            𓋹 {book.added_on}
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    if st.button("✕", key=f"del_{book.id}"):
                        delete_book(book.id)
                        st.rerun()
    else:
        st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #666;">
                𓁶 No scrolls found in this cosmic quadrant
            </div>
        """, unsafe_allow_html=True)

# Statistics Section
st.markdown("---")
st.markdown("### 𓇽 Cosmic Insights")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="metric-card hover-glow">
            <div style="font-size: 2em;">📚</div>
            <h3>{len(books)}</h3>
            <p style="color: #aaa;">Total Codices</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    genre_counts = pd.Series([book.genre for book in books]).value_counts()
    st.markdown(f"""
        <div class="metric-card hover-glow">
            <div style="font-size: 2em;">🌐</div>
            <h3>{len(genre_counts)}</h3>
            <p style="color: #aaa;">Cosmic Categories</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card hover-glow">
            <div style="font-size: 2em;">🕰️</div>
            <h3>{pd.to_datetime([book.added_on for book in books]).max().strftime('%Y') if books else 'N/A'}</h3>
            <p style="color: #aaa;">Current Era</p>
        </div>
    """, unsafe_allow_html=True)

# Interactive 3D Chart
st.markdown("---")
st.markdown("### 𓍝 Galactic Distribution")
if books:
    fig = px.pie(names=genre_counts.index, values=genre_counts.values, 
                hole=0.4, color=genre_counts.index,
                color_discrete_sequence=px.colors.sequential.Plasma_r)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white'), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.markdown("""
        <div style="text-align: center; padding: 2rem; color: #666;">
            𓁶 No data to display cosmic distribution
        </div>
    """, unsafe_allow_html=True)

# Floating Export Button
st.markdown("""
    <div style="position: fixed; bottom: 20px; right: 20px; z-index: 999;">
        <a href="data:text/csv;base64,{b64}" download="library_collection.csv" style="text-decoration: none;">
            <button style="background: linear-gradient(45deg, #7F00FF, #E100FF); 
                    border: none; padding: 15px 30px; border-radius: 25px; color: white; cursor: pointer; 
                    box-shadow: 0 8px 25px rgba(127, 0, 255, 0.3);">
                📥 Download Cosmic Archive
            </button>
        </a>
    </div>
""".format(b64=export_books().decode()), unsafe_allow_html=True)