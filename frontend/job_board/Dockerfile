FROM node:20-alpine

WORKDIR /app/frontend

COPY package.json package-lock.json ./

COPY . ./

RUN npm install

RUN npm run build

ENV HOST=0.0.0.0

EXPOSE 5173

CMD ["npm", "run", "dev"]