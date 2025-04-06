from fpdf import FPDF
import tempfile
import os

def generate_pdf_report(df, data_types, image_list, st):
    st.sidebar.header("📄 Export Report")
    if st.sidebar.button("Generate PDF Report"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "ZecData EDA Summary Report", ln=True, align='C')

        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}", ln=True)
        pdf.ln(5)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Column Types", ln=True)
        pdf.set_font("Arial", '', 11)

        for col, typ in data_types.items():
            line = f"{col} - {typ}"
            safe_line = line.encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(0, 8, safe_line, ln=True)

        if image_list:
            pdf.add_page()
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Embedded Visualizations", ln=True)

            for img in image_list:
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
                        img_path = tmp_img.name
                        img.save(img_path)

                    img.close()  # Make sure the image is closed before use
                    pdf.image(img_path, w=180)

                    try:
                        os.remove(img_path)
                    except PermissionError:
                        pass  # Ignore if file can't be deleted right now
                except Exception as e:
                    st.warning(f"⚠️ Could not embed one image: {e}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp_path = tmp.name
            pdf.output(tmp_path)

        with open(tmp_path, "rb") as f:
            st.sidebar.download_button("📥 Download PDF Report", f.read(), file_name="EDA_Report.pdf", mime="application/pdf")

        try:
            os.remove(tmp_path)
        except PermissionError:
            pass  # PDF file still open or locked
