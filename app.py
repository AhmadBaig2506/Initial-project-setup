
import streamlit as st

from pipeline import run_retrieval


st.set_page_config(
    page_title="On-Device AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 On-Device AI Research Assistant")

st.write(
    "Research questions using web search, "
    "text extraction, and local BM25 ranking."
)

question = st.text_input(
    "Enter your research question:",
    placeholder="What causes sleep apnea?"
)

if st.button("Research", type="primary"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching and ranking evidence..."):
            result = run_retrieval(question)

        passages = result["passages"]

        if not passages:
            st.error(
                "No evidence was retrieved. "
                "Please try another question."
            )
            st.stop()

        st.success("Research completed!")

        # Processing statistics
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Search Results",
            result["sources_found"]
        )

        col2.metric(
            "Text Chunks",
            result["chunks_created"]
        )

        col3.metric(
            "Processing Time",
            f"{result['elapsed_seconds']:.2f}s"
        )

        st.divider()

        st.subheader("Top Relevant Evidence")

        for index, doc in enumerate(passages, start=1):

            with st.expander(
                f"{index}. {doc['title']}",
                expanded=(index == 1)
            ):
                st.write(doc["text"])

                st.caption(
                    f"BM25 relevance score: "
                    f"{doc['score']:.4f}"
                )

                st.markdown(
                    f"[View original source]({doc['url']})"
                )

        st.divider()

        st.info(
            "AI-generated summaries will be added "
            "when the local model is integrated."
        )
