import React, { useState } from "react";

export default function Login() {
  const [signIn, setSignin] = useState(true);

  const styles = {
    padding: 10,
    margin: 10,
  };

  function LoginUser() {
    return (
      <div>
        <h1>Login</h1>
        <form>
          <div style={styles}>
            <label htmlFor="email">Email</label>
            <input type="email" id="email" name="email" />
            <br />
          </div>
          <div style={styles}>
            <label htmlFor="password">Password</label>
            <input type="password" id="password" name="password" />
            <br />
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
    );
  }

  function RegisterUser() {

    
    return (
      <div>
        <h1>Register</h1>
        <form>

          <label htmlFor="user">User</label>
          <input type="text" id="user" name="User" />
          <br />

          <label htmlFor="role">Role</label>
          <input type="text" id="role" name="role" />
          <br />

          <label htmlFor="email">Email</label>
          <input type="email" id="email" name="email" />
          <br />

          <label htmlFor="password">Password</label>
          <input type="password" id="password" name="password" />
          <br />

          <button type="submit">Register</button>
        </form>
      </div>
    );
  }

  return (
    <>
      {signIn ? <LoginUser /> : <RegisterUser />}
      <div onClick={() => setSignin(!signIn)} styles={{ cursor: "pointer" }}>
        <h6>{signIn ? "Register" : "Signin"}</h6>
      </div>
    </>
  );
}
