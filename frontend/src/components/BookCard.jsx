import { useState } from 'react'
import api from '../api'

export default function BookCard({ book, onSubmitted }) {
  const [open, setOpen] = useState(false)
  const [email, setEmail] = useState('')
  const [mobile, setMobile] = useState('')
  const [message, setMessage] = useState('')

  const submit = async (e) => {
    e.preventDefault()
    try {
      await api.post('requests/', { book: book.id, email, mobile })
      setMessage('Request submitted!')
      setEmail('')
      setMobile('')
      onSubmitted?.()
    } catch {
      setMessage('Submission failed.')
    }
  }

  return (
    <div className="card">
      <img src={book.image_src || 'https://via.placeholder.com/300x180?text=No+Image'} alt={book.title} />
      <h3>{book.title}</h3>
      <p>{book.author}</p>
      <p>{book.description}</p>
      <p>{book.is_available ? 'Available' : 'Not Available'}</p>
      <button onClick={() => setOpen(true)} disabled={!book.is_available}>Read The Book</button>

      {open && (
        <div className="modal">
          <div className="modal-content">
            <h3>Request: {book.title}</h3>
            <form onSubmit={submit}>
              <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
              <input type="tel" value={mobile} onChange={e => setMobile(e.target.value)} placeholder="Mobile" required />
              <p>{message}</p>
              <button type="submit">Submit</button>
              <button type="button" onClick={() => setOpen(false)}>Cancel</button>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
