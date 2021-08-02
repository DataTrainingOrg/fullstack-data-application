import http from "../http-common";

const getAll = () => {
  return http.get("/posts");
};

const get = id => {
  return http.get(`/posts/${id}`);
};

const create = data => {
  return http.post("/posts", data);
};

const update = (id, data) => {
  return http.put(`/posts/${id}`, data);
};

const remove = id => {
  return http.delete(`/posts/${id}`);
};

const removeAll = () => {
  return http.delete(`/posts`);
};

const findByTitle = title => {
  return http.get(`/posts?title=${title}`);
};

export default {
  getAll,
  get,
  create,
  update,
  remove,
  removeAll,
  findByTitle
};