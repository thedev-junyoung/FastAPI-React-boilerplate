/* 

상태 관리: username, email, password 상태를 관리합니다. 폼이 제출되면 handleSubmit 함수가 호출되어 사용자 데이터를 서버로 전송합니다.
props: user, setUser, fetchUsers를 부모 컴포넌트로부터 받아 사용합니다.
폼 제출: 사용자가 폼을 제출하면, POST 또는 PUT 요청을 통해 서버에 사용자 데이터를 전송합니다.

*/
import React, { useState } from 'react';
import axios from 'axios';

function UserForm({ user, setUser, fetchUsers }) {
  // useState 훅을 사용하여 로컬 상태를 관리합니다.
  const [username, setUsername] = useState(user ? user.username : '');  // 사용자명 상태
  const [email, setEmail] = useState(user ? user.email : '');  // 이메일 상태
  const [password, setPassword] = useState('');  // 비밀번호 상태

  // 폼 제출 이벤트 핸들러
  const handleSubmit = async (event) => {
    event.preventDefault();  // 기본 폼 제출 동작을 방지합니다.
    const userData = {
      username,
      email,
      password
    };

    try {
      if (user) {
        // 기존 사용자 업데이트 요청
        await axios.put(`http://localhost:8000/api/v1/users/${user.id}`, userData);
      } else {
        // 새로운 사용자 생성 요청
        await axios.post('http://localhost:8000/api/v1/users/', userData);
      }
      fetchUsers();  // 사용자 목록을 다시 가져옵니다.
      setUser(null);  // 폼을 초기 상태로 리셋합니다.
    } catch (error) {
      console.error("Failed to submit user data:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export default UserForm;

