import streamlit as st
import os
from pathlib import Path
import subprocess

# 配置
DOCS_DIR = Path("docs")
COURSES = {
    "易经个人成长课": "个人成长课",
    "易经判断力课": "判断力课",
    "易经关系婚姻课": "关系婚姻课",
    "易经风水实用课": "风水实用课"
}

st.set_page_config(
    page_title="易经课程管理系统",
    page_icon="📚",
    layout="wide"
)

st.title("📚 易经课程管理系统")

# 侧边栏 - 课程选择
st.sidebar.header("课程管理")
selected_course = st.sidebar.selectbox(
    "选择课程",
    list(COURSES.keys())
)

course_folder = DOCS_DIR / COURSES[selected_course]

# 获取课程文件列表
def get_course_files(folder):
    if not folder.exists():
        return []
    return sorted([f for f in folder.glob("*.md")])

files = get_course_files(course_folder)

# 主界面
tab1, tab2, tab3 = st.tabs(["📝 编辑文章", "➕ 新建文章", "🚀 发布"])

# Tab 1: 编辑现有文章
with tab1:
    if files:
        selected_file = st.selectbox(
            "选择要编辑的文章",
            files,
            format_func=lambda x: x.name
        )

        if selected_file:
            st.subheader(f"编辑：{selected_file.name}")

            # 读取文件内容
            content = selected_file.read_text(encoding='utf-8')

            # 编辑器
            new_content = st.text_area(
                "文章内容",
                content,
                height=500,
                help="支持 Markdown 格式"
            )

            col1, col2 = st.columns([1, 5])
            with col1:
                if st.button("💾 保存", type="primary"):
                    selected_file.write_text(new_content, encoding='utf-8')
                    st.success(f"✅ 已保存：{selected_file.name}")

            with col2:
                if st.button("🔄 重置"):
                    st.rerun()
    else:
        st.info(f"📭 {selected_course} 目前没有文章")

# Tab 2: 新建文章
with tab2:
    st.subheader("新建文章")

    new_filename = st.text_input(
        "文件名",
        placeholder="例如：第01讲-标题.md",
        help="请输入文件名，必须以 .md 结尾"
    )

    new_content = st.text_area(
        "文章内容",
        height=400,
        placeholder="在这里输入文章内容...",
        help="支持 Markdown 格式"
    )

    if st.button("✨ 创建文章", type="primary"):
        if new_filename and new_content:
            if not new_filename.endswith('.md'):
                st.error("❌ 文件名必须以 .md 结尾")
            else:
                new_file_path = course_folder / new_filename
                if new_file_path.exists():
                    st.error(f"❌ 文件已存在：{new_filename}")
                else:
                    new_file_path.write_text(new_content, encoding='utf-8')
                    st.success(f"✅ 已创建：{new_filename}")
                    st.balloons()
        else:
            st.warning("⚠️ 请填写文件名和内容")

# Tab 3: 发布到网站
with tab3:
    st.subheader("发布到网站")

    st.info("💡 点击下方按钮将所有修改推送到 GitHub，网站会自动更新（约1-2分钟）")

    # 显示当前状态
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
            cwd="."
        )

        if result.stdout.strip():
            st.warning("📝 有未提交的修改：")
            st.code(result.stdout, language="text")

            commit_message = st.text_input(
                "提交说明",
                value="更新课程内容",
                help="描述本次修改的内容"
            )

            if st.button("🚀 推送到网站", type="primary"):
                with st.spinner("正在推送..."):
                    # Git add
                    subprocess.run(["git", "add", "-A"], cwd=".")

                    # Git commit
                    subprocess.run(
                        ["git", "commit", "-m", commit_message],
                        cwd="."
                    )

                    # Git push
                    push_result = subprocess.run(
                        ["git", "push", "origin", "master"],
                        capture_output=True,
                        text=True,
                        cwd="."
                    )

                    if push_result.returncode == 0:
                        st.success("✅ 推送成功！网站将在1-2分钟内更新")
                        st.balloons()
                    else:
                        st.error(f"❌ 推送失败：{push_result.stderr}")
        else:
            st.success("✅ 没有需要推送的修改")

    except Exception as e:
        st.error(f"❌ 错误：{str(e)}")

# 底部信息
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 统计信息")
for course_name, folder_name in COURSES.items():
    folder = DOCS_DIR / folder_name
    if folder.exists():
        count = len(list(folder.glob("*.md")))
        st.sidebar.markdown(f"**{course_name}**: {count} 篇")
