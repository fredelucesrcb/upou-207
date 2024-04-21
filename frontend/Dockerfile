FROM node:20-alpine

WORKDIR /frontend

COPY ./package*.json .

RUN npm install
# RUN npm install react-scripts -g --silent

COPY . .

# EXPOSE 3000

CMD ["npm", "start"]