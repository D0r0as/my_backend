FROM python:3.11.2-buster
ENV DEBIAN_FRONTEND='noninteractive'
RUN apt-get update && apt install -y curl libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
RUN curl -sSL https://install.python-poetry.org | python
ENV PATH="${PATH}:/root/.local/bin"
COPY ./src /app/src
COPY alembic.ini /app/
COPY migration /app/migration
COPY pyproject.toml /app/
ENV PYTHONPATH /app/
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-root
RUN chmod +x ./src/start.sh
EXPOSE 8000
