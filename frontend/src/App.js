/* 

상태 관리: users와 editingUser 상태를 관리합니다.
데이터 가져오기: fetchUsers 함수는 서버에서 사용자 목록을 가져와 users 상태를 업데이트합니다.
컴포넌트 구조: UserForm과 UserList 컴포넌트를 포함하여 전체적인 사용자 관리 기능을 제공합니다.
useEffect: 컴포넌트가 처음 마운트될 때 fetchUsers 함수를 호출하여 사용자 목록을 가져옵니다.
*/

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserForm from './components/UserForm';
import UserList from './components/UserList';

function App() {
  // useState 훅을 사용하여 사용자 목록과 편집할 사용자 상태를 관리합니다.
  const [users, setUsers] = useState([]);  // 사용자 목록 상태
  const [editingUser, setEditingUser] = useState(null);  // 편집할 사용자 상태

  // 사용자 목록을 가져오는 비동기 함수
  const fetchUsers = async () => {
    try {
      const result = await axios.get('http://localhost:8000/api/v1/users/');
      setUsers(result.data);  // 사용자 목록 상태를 업데이트합니다.
    } catch (error) {
      console.error("Failed to fetch users:", error);
    }
  };

  // 컴포넌트가 마운트될 때 사용자 목록을 가져옵니다.
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      <h1>Users</h1>
      {/* 사용자 생성 및 업데이트 폼 */}
      <UserForm
        user={editingUser}
        setUser={setEditingUser}
        fetchUsers={fetchUsers}
      />
      {/* 사용자 목록 */}
      <UserList
        users={users}
        setEditingUser={setEditingUser}
        fetchUsers={fetchUsers}
      />
    </div>
  );
}

export default App;
