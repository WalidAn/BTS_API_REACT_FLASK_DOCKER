FROM node:18-alpine

WORKDIR /app

# Installer les dépendances
COPY package*.json /app/
RUN npm install

# Copier le reste du code
COPY . /app

# Vite en mode dev (port 5173)
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
