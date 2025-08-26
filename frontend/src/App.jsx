import { useEffect, useState } from 'react'
import api from './api'
import BookCard from './components/BookCard'

export default function App() {
  const [books, setBooks] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [q, setQ] = useState('')

  const fetchBooks = async () => {
    setLoading(true)
    setError('')
    try {
      const { data } = await api.get('books/', { params: q ? { q } : {} })
      setBooks(data)
    } catch {
      setError('Failed to load books.')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { fetchBooks() }, [])

  return (
    <div>
      <header>
        <h1>Library</h1>
        <p>{books.length} books</p>
      </header>
      <div>
        <input value={q} onChange={e => setQ(e.target.value)} placeholder="Search" />
        <button onClick={fetchBooks}>Search</button>
      </div>
      {loading && <p>Loading…</p>}
      {error && <p>{error}</p>}
      <div className="grid grid-3">
        {books.map(b => <BookCard key={b.id} book={b} onSubmitted={fetchBooks} />)}
      </div>
    </div>
  )
}
