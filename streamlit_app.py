import streamlit as st
from utils.data import get_tickers
from utils.filters import get_top20_by_volume
from utils.export import export_to_excel

st.title("台股 15 分 K 靠近 60MA 股票排行")
st.caption("依日K成交量排序，顯示前 20 名")

if st.button("開始分析"):
    with st.spinner("資料抓取中..."):
        codes = get_tickers()
        result = get_top20_by_volume(codes)
        if not result.empty:
            st.subheader("結果表格")
            st.dataframe(result)

            # 匯出 Excel
            filepath = export_to_excel(result)
            with open(filepath, "rb") as f:
                st.download_button("下載 Excel", f, file_name="near_60ma_top20.xlsx")
        else:
            st.warning("找不到符合條件的股票，請稍後再試。")
