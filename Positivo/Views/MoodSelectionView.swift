import SwiftUI

struct MoodSelectionView: View {
    private let columns = [
        GridItem(.flexible()),
        GridItem(.flexible()),
        GridItem(.flexible()),
    ]

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                Text("How are you feeling today?")
                    .font(.title2)
                    .fontWeight(.semibold)
                    .padding(.top, 16)

                LazyVGrid(columns: columns, spacing: 16) {
                    ForEach(Mood.allCases) { mood in
                        NavigationLink(value: mood) {
                            VStack(spacing: 8) {
                                Text(mood.emoji)
                                    .font(.system(size: 36))
                                Text(mood.displayName)
                                    .font(.caption)
                                    .fontWeight(.medium)
                            }
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 16)
                            .background(Color(.systemGray6))
                            .cornerRadius(16)
                        }
                        .buttonStyle(.plain)
                    }
                }
                .padding(.horizontal)
            }
        }
        .navigationTitle("Positivo")
        .navigationDestination(for: Mood.self) { mood in
            QuoteView(mood: mood)
        }
    }
}

#Preview {
    NavigationStack {
        MoodSelectionView()
    }
}
