import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Servicio predictivo del precio de alquiler de coches según el área geográfica')
    st.image('mapa.jpg', caption='Imagen de Europa', use_column_width=True)
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')

    opcion = st.radio('Seleccione el servicio:',
                      ('Predicción del precio (con CSV)', 'Predicción del precio (manualmente)'),
                      index=0,
                      key='option')

    if st.button('OK'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Predicción del precio (con CSV)':
        switch_page("pred_precio_csv")
    elif opcion == 'Predicción del precio (manualmente)':
        switch_page("pred_precio_man")


if __name__ == "__main__":
    main()
