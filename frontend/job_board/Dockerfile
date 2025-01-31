FROM node:18

WORKDIR /app/frontend

COPY package.json package-lock.json ./

COPY . ./

RUN npm install

RUN npx eslint . --ext .js,.jsx,.ts,.tsx || true

ENV HOST=0.0.0.0

EXPOSE 5173

CMD ["npm", "run", "dev"]