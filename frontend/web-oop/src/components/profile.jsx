import { useEffect, useState } from 'react';

function ProfilePage(props) {
  const [account, setAccount] = useState(null);
  const [role, setRole] = useState('');

  

  const getdata = function()  {
    const storedAccount = JSON.parse(localStorage.getItem('account'));
    const storedRole = localStorage.getItem('role');

    setAccount(storedAccount);
    setRole(storedRole);
    console.log(account)
  }

  useEffect(() => {
    
    getdata();


  }, []);

  if (!account || !role) {
    getdata();
    return <div>Loading...</div>;
  }

  return (
    <div className="bg-gray-100 h-screen">
      <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <h1 className="text-2xl font-bold">{account._Customer__name}'s Profile</h1>
          <p className="text-gray-500 mt-2">{account._Customer__email}</p>
        </div>
        <div className="bg-white shadow overflow-hidden sm:rounded-lg">
          <div className="px-4 py-5 sm:grid sm:grid-cols-2">
            <h3 className="text-lg leading-6 font-medium text-gray-900">Account Information</h3>
            <p className="mt-1 max-w-2xl text-sm text-gray-500 sm:col-span-2">View and update your account information.</p>
            <button href="#edit" onClick={props.loginclick} className="col-span-2 justify-end" class="rounded-none ..." >Edit Profile</button>
          </div>
          <div className="border-t border-gray-200">
            <dl>
              <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-sm font-medium text-gray-500">Name</dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{account._Customer__name}</dd>
              </div>
              <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-sm font-medium text-gray-500">Email address</dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{account._Customer__email}</dd>
              </div>
              <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                <dt className="text-sm font-medium text-gray-500">Address</dt>
                <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">{account._Customer__address}</dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProfilePage;
