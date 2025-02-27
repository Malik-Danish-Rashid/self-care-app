import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Self-Care App", layout="wide")

page_bg_img = f'''
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://github.com/Malik-Danish-Rashid/self-care-app/blob/main/Flux_Dev_Create_a_serene_and_uplifting_illustration_that_embod_0.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}
[data-testid="stSidebar"] {{
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 15px;
    padding: 20px;
}}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    st.title("🌿 Self-Care Application")
    st.subheader(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    categories = {
        "🏃 Physical Health": ["Morning Exercise", "Drink Water", "Eat Healthy", "Go for a Walk", "Get Enough Sleep"],
        "📚 Learning Skills": ["Read a Book", "Practice Coding", "Learn New Words", "Watch Educational Video", "Solve Puzzles"],
        "🎮 Entertainment": ["Listen to Music", "Watch a Movie", "Play a Game", "Draw or Paint", "Spend Time with Friends"]
    }
    st.sidebar.title("✅ Task Categories")
    completed_tasks = 0
    total_tasks = sum(len(tasks) for tasks in categories.values())
    
    for category, tasks in categories.items():
        st.sidebar.subheader(category)
        for task in tasks:
            if st.sidebar.checkbox(task):
                completed_tasks += 1
    
    progress = (completed_tasks / total_tasks) * 100 if total_tasks else 0
    st.progress(progress / 100)
    
    st.write(f"### 🌟 Tasks Completed: {completed_tasks}/{total_tasks} ({progress:.0f}%)")
    
    if progress >= 70:
        st.success("🚀 Perfect! Keep it up!")
    elif progress >= 40:
        st.info("👍 Good Job! You're on the right track!")
    else:
        st.warning("🔥 You can do it! Keep pushing!")
    
    st.write("---")
    st.caption("✨ Noa's Project")
    
if __name__ == "__main__":
    main()
