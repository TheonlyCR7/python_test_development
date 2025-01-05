const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// 模拟用户数据
let users = [
  { id: 1, name: '张三', email: 'zhangsan@example.com', age: 25 },
];

// 创建用户
app.post('/api/users', (req, res) => {
  const user = { id: users.length + 1, ...req.body };
  users.push(user);
  res.status(201).json({ ...user, message: '用户创建成功' });
});

// 查询所有用户
app.get('/api/users', (req, res) => {
  res.json(users);
});

// 查询单个用户
app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: '用户不存在' });
  res.json(user);
});

// 更新用户
app.put('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: '用户不存在' });
  Object.assign(user, req.body);
  res.json({ ...user, message: '用户更新成功' });
});

// 删除用户
app.delete('/api/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ message: '用户不存在' });
  users.splice(index, 1);
  res.json({ message: '用户删除成功' });
});

// 启动服务
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
