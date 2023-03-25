FROM python:3.10

WORKDIR /DRF_stocks_products

COPY ./requirements.txt /DRF_stocks_products/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /DRF_stocks_products

EXPOSE 8000

ENV SECRET_KEY django-insecure-nw^y+m^wmxza1asgk+)!ua2qx9)g+#v=6%76-9i8i(6eqiw94j
ENV DEBUG 1

RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi"]