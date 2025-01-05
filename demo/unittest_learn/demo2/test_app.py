import unittest
from app import app

class LoginTestCase(unittest.TestCase):

    # 设置测试客户端
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # 测试登录成功的情况
    def test_login_success(self):
        response = self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # 应该重定向到 dashboard

    # 测试登录失败的情况
    def test_login_fail(self):
        response = self.client.post('/login', data={'username': 'testuser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 403)  # 登录失败，返回403错误

    # 测试访问 dashboard 页面
    def test_dashboard(self):
        with self.client:
            self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
            response = self.client.get('/dashboard')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Welcome to the Dashboard!', response.data.decode())

if __name__ == '__main__':
    unittest.main()
