/* 

사용자 목록 표시: users 배열을 받아 사용자 목록을 렌더링합니다.
편집: setEditingUser 함수를 사용하여 특정 사용자를 편집 모드로 설정합니다.
삭제: handleDelete 함수가 호출되면, DELETE 요청을 통해 서버에서 사용자를 삭제합니다.

*/
import React from 'react';
import axios from 'axios';

function UserList({ users, setEditingUser, fetchUsers }) {
  // 사용자 삭제 이벤트 핸들러
  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/v1/users/${id}`);
      fetchUsers();  // 사용자 목록을 다시 가져옵니다.
    } catch (error) {
      console.error("Failed to delete user:", error);
    }
  };

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>
          {user.username} - {user.email}
          <button onClick={() => setEditingUser(user)}>Edit</button>  {/* // 편집 모드로 전환합니다. */}
          <button onClick={() => handleDelete(user.id)}>Delete</button>  {/* // 사용자를 삭제합니다. */}
        </li>
      ))}
    </ul>
  );
}

export default UserList;
