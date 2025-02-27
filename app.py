import streamlit as st
from datetime import datetime

def set_bg():
    bg_url = "https://raw.githubusercontent.com/Malik-Danish-Rashid/self-care-app/afb5fc6a12b8a7a702fa8bdc1e93407413d60cd0/pic.png"
    bg_style = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("{bg_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    [data-testid="stSidebar"] {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
    }}
    .main-title {{
        color: #000000;  /* Changed to black */
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }}
    .sub-header {{
        color: #000000;  /* Changed to black */
        text-align: center;
        font-size: 20px;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

def main():
    set_bg() 

    st.markdown('<h1 class="main-title">🌿 Self-Care Application</h1>', unsafe_allow_html=True)
    st.markdown(f'<h3 class="sub-header">📅 Date: {datetime.now().strftime("%Y-%m-%d")}</h3>', unsafe_allow_html=True)

    categories = {
        "💪 Physical Health": ["🏃 Morning Exercise", "💧 Drink Water", "🥗 Eat Healthy", "🚶 Go for a Walk", "😴 Get Enough Sleep"],
        "📚 Learning Skills": ["📖 Read a Book", "💻 Practice Coding", "📝 Learn New Words", "🎥 Watch Educational Video", "🧩 Solve Puzzles"],
        "🎉 Entertainment": ["🎵 Listen to Music", "🎬 Watch a Movie", "🎮 Play a Game", "🎨 Draw or Paint", "👫 Spend Time with Friends"]
    }

    st.sidebar.title("📌 Task Categories")
    completed_tasks = 0
    total_tasks = sum(len(tasks) for tasks in categories.values())

    for category, tasks in categories.items():
        st.sidebar.subheader(category)
        for task in tasks:
            if st.sidebar.checkbox(task):
                completed_tasks += 1
    progress = (completed_tasks / total_tasks) * 100 if total_tasks else 0
    st.progress(progress / 100)
    st.write(f"### ✅ Tasks Completed: {completed_tasks}/{total_tasks} ({progress:.0f}%)")

    if progress >= 70:
        st.success("🎯 Perfect! Keep it up! 💪")
    elif progress >= 40:
        st.info("👍 Good Job! You're on the right track!")
    else:
        st.warning("🔥 You can do it! Keep pushing!")

    st.write("---")
    st.caption("🌱 Made with ❤️ by Noa")

if __name__ == "__main__":
    main()
    st.caption("✨ Noa's Project")
